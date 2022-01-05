"""
Title     : Reverse
Source    : Forritunarkeppni Framhaldsskólanna 2017
URL       : https://open.kattis.com/problems/ofugsnuid
Author    : arsho
Created   : 04 January 2022
"""
n = int(input())
ar = []
for i in range(n):
    ar.append(int(input()))
ar = ar[::-1]
for i in ar:
    print(i)
