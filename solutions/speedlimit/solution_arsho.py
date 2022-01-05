"""
Title     : Speed Limit
Source    : 2004 ACM ICPC Mid-Central North American Regional Contest
URL       : https://open.kattis.com/problems/speedlimit
Author    : arsho
Created   : 04 January 2022
"""
while True:
    number_of_records = int(input())
    if number_of_records == -1:
        break
    previous_time = 0
    total_miles = 0
    for i in range(number_of_records):
        speed, current_time = list(map(int, input().split()))
        total_miles += speed * (current_time - previous_time)
        previous_time = current_time
    print(total_miles, " miles")
