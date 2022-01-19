"""
Title     : Alphabet Spam
Source    : Northwestern Europe Regional Contest (NWERC) 2014 Practice Session
URL       : https://open.kattis.com/problems/alphabetspam
Author    : arsho
Created   : 18 January 2022
"""
import string

line = input()
line_length = len(line)
whitespace_count = 0
lowercase_count = 0
uppercase_count = 0
special_character_count = 0
for c in line:
    if c == '_':
        whitespace_count += 1
    elif c in string.ascii_lowercase:
        lowercase_count += 1
    elif c in string.ascii_uppercase:
        uppercase_count += 1
    else:
        special_character_count += 1
print(whitespace_count / line_length)
print(lowercase_count / line_length)
print(uppercase_count / line_length)
print(special_character_count / line_length)
