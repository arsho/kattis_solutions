"""
Title     : Help a PhD candidate out!
Source    : Nordic Collegiate Programming Contest (NCPC) 2010
URL       : https://open.kattis.com/problems/helpaphd
Author    : arsho
Created   : 04 January 2022
"""
n = int(input())
for i in range(n):
    value = input()
    if value == "P=NP":
        print("skipped")
    else:
        a, b = value.split("+")
        print(int(a) + int(b))
