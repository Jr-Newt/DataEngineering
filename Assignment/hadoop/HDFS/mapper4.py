#!/usr/bin/python3
"""mapper2.py"""
import sys

# input comes from standard input
for line in sys.stdin:
        line = line.strip()
        if line:
                columns = line.split(',')
                if columns[-6] != "storage_issue_reported_l3m,," or columns[-1] != "product_wg_ton":
                        storage_issue = columns[-6].strip()
                        product_wg = columns[-1].strip()
                        print('%s,%s' % (storage_issue, product_wg))

