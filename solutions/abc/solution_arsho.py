"""
Title     : ABC
Source    : Croatian Open Competition in Informatics 2006/2007, contest #2
URL       : https://open.kattis.com/problems/abc
Author    : arsho
Created   : 04 January 2022
"""
values = sorted(list(map(int, input().split())))
order = input()
data = dict(zip("ABC", values))
for c in order:
    print(data[c], end=" ")
