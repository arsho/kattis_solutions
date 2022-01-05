"""
Title     : Bijele
Source    : Croatian Open Competition in Informatics 2007/2008, contest #2
URL       : https://open.kattis.com/problems/bijele
Author    : arsho
Created   : 04 January 2022
"""
found = list(map(int, input().split()))
required = [1, 1, 2, 2, 2, 8]
for i in range(len(found)):
    print(required[i] - found[i], end=" ")
