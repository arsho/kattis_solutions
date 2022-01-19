"""
Title     : A List Game
Source    : Spotify Challenge 2010
URL       : https://open.kattis.com/problems/listgame
Author    : arsho
Created   : 18 January 2022
"""
import math

n = int(input())
i = 2
count = 0
while n > 1 and i <= math.ceil(n ** 0.5):
    if n % i == 0:
        n = n // i
        count += 1
    elif i % 2 == 0:
        i += 1
    else:
        i += 2
if n > 2:
    count += 1
print(count)
