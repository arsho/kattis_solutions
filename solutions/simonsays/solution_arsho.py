"""
Title     : Simon Says
Source    : 2015 ICPC North American Qualifier Contest
URL       : https://open.kattis.com/problems/simonsays
Author    : arsho
Created   : 04 January 2022
"""
number_of_lines = int(input())
for i in range(number_of_lines):
    line = input()
    trigger_text = "Simon says "
    try:
        position = line.index(trigger_text) + len(trigger_text)
        print("".join(line[position:]))
    except:
        pass
