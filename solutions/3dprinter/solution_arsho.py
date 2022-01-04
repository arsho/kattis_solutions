"""
Title     : 3D Printed Statues
Source    : KTH Challenge 2017
URL       : https://open.kattis.com/problems/3dprinter
Author    : arsho
Created   : 04 January 2022
"""
statue_required = int(input())
printers = 1
days = 1
while printers < statue_required:
    printers *= 2
    days += 1
print(days)
