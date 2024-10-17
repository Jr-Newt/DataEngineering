#!/usr/bin/python3
"""mapper2.py"""
import sys

# input comes from standard input
for line in sys.stdin:
        line = line.strip()
        if line:
                columns = line.split(',')
                if columns[7] != "transport_issue_l1y," or columns[-1] != "product_wg_ton":
                        transport_issue = columns[7].strip()
                        product_wg = columns[-1].strip()
                        print('%s,%s' % (transport_issue, product_wg))

