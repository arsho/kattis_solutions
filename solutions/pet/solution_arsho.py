"""
Title     : Pet
Source    : Croatian Open Competition in Informatics 2008/2009, contest #3
URL       : https://open.kattis.com/problems/pet
Author    : arsho
Created   : 05 January 2022
"""
max_score = 0
champion = 1
for i in range(5):
    current_score = sum(list(map(int, input().split())))
    if current_score > max_score:
        max_score = current_score
        champion = i + 1
print(champion, max_score)
