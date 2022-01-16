"""
Title     : Zyxab
Source    : Lokakeppni TÖL607G 2021
URL       : https://open.kattis.com/problems/zyxab
Author    : arsho
Created   : 16 January 2022
"""
from functools import cmp_to_key


def compare_two_names(name_1, name_2):
    if len(name_1) < len(name_2):
        return -1
    elif len(name_1) > len(name_2):
        return 1
    if name_1 > name_2:
        return -1
    elif name_1 < name_2:
        return 1
    return 0


number_of_names = int(input())
game_names = []
for i in range(number_of_names):
    game_name = input()
    if len(game_name) >= 5 and len(set(game_name)) == len(game_name):
        game_names.append(game_name)

game_names = sorted(game_names, key=cmp_to_key(compare_two_names))
if len(game_names) > 0:
    print(game_names[0])
else:
    print("neibb!")
