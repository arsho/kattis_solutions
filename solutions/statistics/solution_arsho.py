"""
Title     : Statistics
Source    : International Collegiate Programming Contest (ACM-ICPC) Dress Rehearsal 2012
URL       : https://open.kattis.com/problems/statistics
Author    : arsho
Created   : 17 January 2022
"""
import sys

total_cases = 0
for line in sys.stdin:
    values = list(map(int, line.split()))[1:]
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    if range_val < 0:
        range_val *= -1
    print(f"Case {total_cases + 1}: {min_val} {max_val} {range_val}")
    total_cases += 1
