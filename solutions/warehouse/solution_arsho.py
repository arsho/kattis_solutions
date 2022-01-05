"""
Title     : Warehouse
Source    : 2018 ICPC South Central USA Regional Contest
URL       : https://open.kattis.com/problems/warehouse
Author    : arsho
Created   : 04 January 2022
"""
test_cases = int(input())
for test_case in range(test_cases):
    sellers = {}
    events = int(input())
    for event in range(events):
        seller, number_of_toys = input().split(" ")
        number_of_toys = int(number_of_toys)
        sellers[seller] = sellers.get(seller, 0) + number_of_toys
    sellers = sorted(sellers.items(), key=lambda x: (-x[1], x[0]))
    print(len(sellers))
    for seller in sellers:
        print(seller[0], seller[1])
