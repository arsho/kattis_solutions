"""
Title     : Ladder
Source    : Spotify Challenge 2010
URL       : https://open.kattis.com/problems/ladder
Author    : arsho
Created   : 18 January 2022
"""
import math

h, v = list(map(int, input().split()))
sin_value = math.sin(math.radians(v))
ladder_length = h / sin_value
ladder_length = math.ceil(ladder_length)
print(ladder_length)