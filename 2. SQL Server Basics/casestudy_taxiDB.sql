DECLARE @Databasename VARCHAR(128) = 'GreenTaxiDB';
IF NOT EXISTs(select 1 FROM sys.databases where name = @Databasename)
BEGIN
	DECLARE @SQL NVARCHAR(MAX)='CREATE DATABASE ' + QUOTENAME(@Databasename);
	EXEC sp_executesql @sql; 
END

use GreenTaxiDB;

CREATE TABLE taxi (
    VendorID INTEGER,
    lpep_pickup_datetime VARCHAR(50),
    lpep_dropoff_datetime VARCHAR(50),
    store_and_fwd_flag VARCHAR(5),
    RatecodeID INTEGER,
    PULocationID INTEGER,
    DOLocationID INTEGER,
    passenger_count INTEGER,
    trip_distance FLOAT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    ehail_fee FLOAT NULL,
    improvement_surcharge FLOAT,
    total_amount FLOAT,
    payment_type INTEGER,
    trip_type INTEGER,
    congestion_surcharge FLOAT
);

BULK INSERT taxi FROM 'D:/2021_Green_Taxi_Trip_Data.csv'
WITH
(
	FIELDTERMINATOR = ',',  -- '|', ';', '\t', ' '
	ROWTERMINATOR ='0x0a',  -- carriage & new Line character - '\r\n', '\' '0x0a'-line feed
	FIRSTROW = 2			--skip the header from records
);

select * from taxi;

-- 1.	Shape of the Table (Number of Rows and Columns)
select count(*) as numofrows from taxi;

select count(*) AS NumofColumns FROM INFORMATION_SCHEMA.columns 
where TABLE_NAME = 'taxi';

--2.  Show Summary of Green Taxi Rides – Total Rides, Total Customers, Total Sales, 
select
	sum(passenger_count) as passengercount,
	sum(total_amount) as amount
from taxi;


--3. Total Rides with Surcharge and its percentage. 
select
	total_amount, congestion_surcharge,
	PERCENT_RANK() over(order by congestion_surcharge desc)
from taxi where congestion_surcharge>0;

--4.	Cumulative Sum of Total Fare Amount for Each Pickup Location
select 
	PULocationID,sum(fare_amount)
	OVER(partition by PULocationID ORDER BY fare_amount asc
	ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
	AS Cummulative_amount
from taxi;

--5.	Which Payment Type is Most Common in Each Drop-off Location
select * from taxi;

select DOLocationID, max(Common_payment) as commn_payment
from
(select DOLocationID ,payment_type, count(*) as Common_payment 
from taxi 
where payment_type is not null
group by DOLocationID, payment_type ) as _
group by DOLocationID
order by DOLocationID

--6.  Create a New Column for Trip Distance Band and Show Distribution

ALTER TABLE taxi ADD Trip_Distance_Band VARCHAR(30)

UPDATE taxi
set Trip_Distance_Band =
case
	when TILE = 1 then 'Long Distance'
	when TILE = 2 then 'Medium Distance'
	else 'Short Distance'
end
from (
	select trip_distance,
	NTILE(3) over(order by trip_distance DESC) as TILE
	from taxi
) AS _

-- 7. Find the Most Frequent Pickup Location (Mode) with rides fare greater than average of ride fare.
select
	PULocationID, count(PULocationID) as pickup
from taxi where fare_amount > (select avg(fare_amount) from taxi)
group by PULocationID order by pickup desc;

-- 8.	Show the Rate Code with the Highest Percentage of Usage
select
	RatecodeID,
	count(RatecodeID) as rate
from taxi
group by RatecodeID
order by rate desc;

-- 9. Show Distribution of Tips, Find the Maximum Chances of Getting a Tip
select
	trip_type, count(tip_amount) as tipcount
from taxi where trip_type is not null
group by trip_type
order by trip_type;

-- 10.	Calculate the Rank of Trips Based on Fare Amount within Each Pickup Location
select 
	PUlocationID, fare_amount,
	rank() over(partition by PUlocationID order by fare_amount)as rank
from taxi;

--11.	Find Top 20 Most Frequent Rides Routes. 

WITH RoutesTable AS
(
SELECT 
	PULocationID,
	DOLocationID,
	COUNT(*) AS Route_Frequency
FROM
	Taxi
GROUP BY
	PULocationID,
	DOLocationID
)
SELECT TOP 20 *
FROM RoutesTable
ORDER BY Route_Frequency DESC;

-- 12.	Calculate the Average Fare of Completed Trips vs. Cancelled Trips
with cancelCTE as(select avg(fare_amount) as tripcancelled from taxi where trip_distance=0),
	 completeCTE as (select avg(fare_amount) as completetrip from taxi where trip_distance!=0)
select
	(select completetrip from completeCTE) as tripCompleted,
	(select tripcancelled from cancelCTE) as tripcancel


--13.	Rank the Pickup Locations by Average Trip Distance and Average Total Amount.

select PULocationID, avg(trip_distance) as avg_trip_dist, avg(total_amount) as avg_total_amt,
dense_rank() over(order by avg(trip_distance) desc,avg(total_amount) desc) 
as PU_rank from taxi group by PULocationID;

-- 14.	Find the Relationship Between Trip Distance & Fare Amount
select
	trip_distance, avg(fare_amount) as relationship
from taxi group by trip_distance;

--15)Identify Trips with Outlier Fare Amounts within Each Pickup Location
select 
	PULocationID, 
	max(total_amount) as total_amount
from taxi 
group by PULocationID 
order by total_amount desc;

select PULocationID, fare_amount from
(select PULocationID, fare_amount,
	PERCENTILE_CONT(0.25)  WITHIN GROUP (ORDER BY fare_amount) OVER() as Q1,
	PERCENTILE_CONT(0.5)  WITHIN GROUP (ORDER BY fare_amount) OVER() as Q2,
	PERCENTILE_CONT(0.75)  WITHIN GROUP (ORDER BY fare_amount) OVER() as Q3,
	PERCENTILE_CONT(0.75)  WITHIN GROUP (ORDER BY fare_amount) OVER() -
	PERCENTILE_CONT(0.25)  WITHIN GROUP (ORDER BY fare_amount) OVER() as IQR
from taxi) Quartiles
where fare_amount < Q1 - 1.5*IQR or fare_amount > Q3 + 1.5*IQR
order by fare_amount

--16)Categorize Trips Based on Distance Travelled
select 
	trip_distance ,
	tile,
case
	when tile>=3 then 'large'
	when tile>=2 then 'medium'
	else 'low'
end as category
from(
	select trip_distance ,ntile(3) over (order by trip_distance) as tile from taxi)
as TileCTE;


--17)Top 5 Busiest Pickup Locations, Drop Locations with Fare less than median total fare
with medianfare as 
	(select PERCENTILE_CONT(0.5) within group (order by total_amount) over() 
	as MedianPrice
	from taxi)
select top(5) 
	PULocationID, 
	DOLocationID, 
	total_amount 
from taxi 
where total_amount<(select max(MedianPrice) from medianfare) and total_amount>0 
order by total_amount desc;

--18)Distribution of Payment Types
select 
	payment_type, 
	count(*) as count_type 
from taxi 
group by(payment_type)
order by payment_type;

--19)Trips with Congestion Surcharge Applied and Its Percentage Count.
select 
	PULocationID, 
	congestion_surcharge,
case
	when total_amount>0 then (congestion_surcharge * 100.0 / total_amount)
	else 0
end as percentag
from taxi 
where congestion_surcharge>0;

--20)Top 10 Longest Trip by Distance and Its summary about total amount.
select top(10) 
	trip_distance,
	total_amount 
from taxi 
order by trip_distance desc;

--21)Trips with a Tip Greater than 20% of the Fare
select 
	PULocationID, 
	tip_amount,
	((tip_amount * 100.0 / total_amount)) as perc
from taxi 
where total_amount>0 and tip_amount>0 and (tip_amount * 100.0 / total_amount)>20
order by PULocationID;

--22)Average Trip Duration by Rate Code
select 
	RatecodeID, 
	avg(datediff(MINUTE,lpep_pickup_datetime,lpep_dropoff_datetime))as avg_diff 
from taxi 
group by RatecodeID 
order by RatecodeID;


--23)Total Trips per Hour of the Day
select 
	DATEPART(HOUR,lpep_pickup_datetime ) as newtime,
	count(DATEPART(HOUR,lpep_pickup_datetime )) as counts 
from taxi 
group by DATEPART(HOUR,lpep_pickup_datetime ) 
order by counts desc;


--24)Show the Distribution about Busiest Time in a Day.
select 
	convert(VARCHAR(8),lpep_pickup_datetime,108) as newtime,
	count( CONVERT(VARCHAR(8),lpep_pickup_datetime,108)) as counts 
from taxi 
group by lpep_pickup_datetime 
order by counts desc;






