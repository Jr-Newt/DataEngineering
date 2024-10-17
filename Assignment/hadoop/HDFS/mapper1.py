#!/usr/bin/python3
"""mapper1.py"""
import sys

# input comes from standard input
for line in sys.stdin:
	line = line.strip()
	if line:
		columns = line.split(',')
		if columns[4] != "zone" or columns[5] != "WH_regional_zone" or columns[-1] != "product_wg_ton":
			zone = columns[4].strip()
			regional_zone = columns[5].strip()
			product_wg = columns[-1].strip()
			print('%s,%s,%s' % (zone, regional_zone, product_wg))