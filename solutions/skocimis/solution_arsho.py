"""
Title     : Skocimis
Source    : Croatian Open Competition in Informatics 2008/2009, contest #1
URL       : https://open.kattis.com/problems/skocimis
Author    : arsho
Created   : 04 January 2022
"""
a, b, c = sorted(list(map(int, input().split())))
print(max(b - a, c - b) - 1)
