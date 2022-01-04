"""
Title     : Odd Echo
Source    : Principles of Algorithmic Problem Solving
URL       : https://open.kattis.com/problems/oddecho
Author    : arsho
Created   : 04 January 2022
"""
n = int(input())
for i in range(n):
    word = input()
    if i % 2 == 0:
        print(word)
