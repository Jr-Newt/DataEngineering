#!/usr/bin/python3
"""mapper2.py"""
import sys
# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # If the line is not empty
    if line:
        columns = line.split(',')
        if columns:
            capacity_size = columns[3].strip()
            num_refill_req_l3m = columns[6].strip()
            ton = columns[-1].strip()

            if capacity_size != "capacity_size" and num_refill_req_l3m != "num_refill_req_l3m":
                print('%s,%s,%s' % (capacity_size, num_refill_req_l3m, ton))
