"""
Title     : Akcija
Source    : Croatian Open Competition in Informatics 2015/2016, contest #1
URL       : https://open.kattis.com/problems/akcija
Author    : arsho
Created   : 15 January 2022
"""
n = int(input())
ar = []
for i in range(n):
    ar.append(int(input()))
ar = sorted(ar, reverse=True)
minimum_value = 0
count = 0
for i in range(n):
    if count != 2:
        minimum_value += ar[i]
        count += 1
    else:
        count = 0
print(minimum_value)
