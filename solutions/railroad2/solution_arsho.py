"""
Title     : Railroad
Source    : 2016 Virginia Tech High School Programming Contest
URL       : https://open.kattis.com/problems/railroad2
Author    : arsho
Created   : 04 January 2022
"""
x, y = list(map(int, input().split()))
if y % 2 != 0:
    print("impossible")
else:
    print("possible")
