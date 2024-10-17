#!/usr/bin/python3
"""reducer1.py"""
import sys
from collections import defaultdict

zone = None
reg_zn = None
zone_wt = defaultdict(lambda: defaultdict(list))

# Read input from stdin
for line in sys.stdin:
    zone, reg_zn, weight = line.strip().split(',')
    try:
        weight = float(weight)
        zone_wt[zone][reg_zn].append(weight)
    except ValueError:
        continue


for zone, WH in zone_wt.items():
    for region, weights in WH.items():
        total = sum(weights)
        print(f"Zone: {zone}\tRegional Zone: {region}\tTotal Product Weight: {total:.2f}")

