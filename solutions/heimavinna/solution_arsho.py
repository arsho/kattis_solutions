"""
Title     : Homework
Source    : Forritunarkeppni Framhaldsskólanna 2019
URL       : https://open.kattis.com/problems/heimavinna
Author    : arsho
Created   : 04 January 2022
"""
problems = input()
count_problems = 0
for chunks in problems.split(";"):
    ranges = chunks.split("-")
    if len(ranges) > 1:
        count_problems += int(ranges[-1]) - int(ranges[0]) + 1
    else:
        count_problems += 1
print(count_problems)
