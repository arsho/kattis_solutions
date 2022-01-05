"""
Title     : A Different Problem
Source    : Kattis
URL       : https://open.kattis.com/problems/different
Author    : arsho
Created   : 04 January 2022
"""
from sys import stdin

for line in stdin:
    if line == '':
        break
    a, b = list(map(int, line.split()))
    print(abs(a - b))
