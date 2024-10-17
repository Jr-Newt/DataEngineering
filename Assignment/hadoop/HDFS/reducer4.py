#!/usr/bin/python3
"""reducer4.py"""
import sys
from collections import defaultdict

issues = None
wt_issue = defaultdict(float)
ct_issue = defaultdict(float)


for line in sys.stdin:
	issues, weight = line.strip().split(',')
	try:
		issues = int(issues)
		weight = float(weight)
		if issues > 0:
			wt_issue[issues] += weight
			ct_issue[issues] += 1
	except ValueError:
        	continue

wt_issue = dict(sorted(wt_issue.items(), key=lambda x: x[0]))

for val in wt_issue:
	print(f"Storage Issues: {val}\t Average Product Weight: {wt_issue[val]/ct_issue[val]:.2f}\t total weight:{wt_issue[val]}")
