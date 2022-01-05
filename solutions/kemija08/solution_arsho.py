"""
Title     : Kemija
Source    : Croatian Open Competition in Informatics 2008/2009, contest #3
URL       : https://open.kattis.com/problems/kemija08
Author    : arsho
Created   : 05 January 2022
"""
line = input().split()
decoded_words = []
for encoded_word in line:
    decoded_word = ""
    position = 0
    while position < len(encoded_word):
        decoded_word += encoded_word[position]
        current_char = encoded_word[position]
        if current_char in 'aeiou':
            position += 3
        else:
            position += 1
    decoded_words.append(decoded_word)
print(" ".join(decoded_words))
