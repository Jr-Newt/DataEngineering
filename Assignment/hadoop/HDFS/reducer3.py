#!/usr/bin/python3
"""reducer3.py"""
import sys
from collections import defaultdict

issues = None
wt_issues = defaultdict(list)
ct_issue = defaultdict(int)

for line in sys.stdin:
    issues, weight = line.strip().split(',')
    try:
        weight = float(weight)
        if int(issues) > 0:
            wt_issues[issues].append(weight)
            ct_issue[issues] += 1
    except ValueError:
        continue

wt_issues = dict(sorted(wt_issues.items(), key=lambda x: x[0]))


for val in wt_issues:
    weights = wt_issues[val]
    average_weight = sum(weights) / len(weights)
    print(f"Transport Issues: {val}\t Average Product Weight: {average_weight}")

