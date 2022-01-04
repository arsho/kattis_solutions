"""
Title     : Above Average
Source    : Waterloo Programming Contest 2002-09-28
URL       : https://open.kattis.com/problems/aboveaverage
Author    : arsho
Created   : 04 January 2022
"""
test_cases = int(input())
for test_case in range(test_cases):
    ar = list(map(int, input().split()))
    total_students = ar[0]
    marks = ar[1:]
    avg_mark = sum(marks) / total_students
    above_avg_students = 0
    for mark in marks:
        if mark > avg_mark:
            above_avg_students += 1
    percentage_above_avg_students = (above_avg_students / total_students) * 100
    print(f"{percentage_above_avg_students:.3f}%")
