"""
Title     : Digit Swap
Source    : Principles of Algorithmic Problem Solving
URL       : https://open.kattis.com/problems/digitswap
Author    : arsho
Created   : 04 January 2022
"""
val = int(input())
reverse_val = (val % 10) * 10 + val // 10
print(reverse_val)
