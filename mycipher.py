#!/usr/bin/python3

import sys

if len(sys.argv) == 2:
    key = sys.argv[1]
    msg = input()
    msg = msg.upper()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decoded = ""

    for i in range(len(msg)):
        if msg[i].isalpha():
            decoded += msg[i]

    word = ""
    for i in range(len(decoded)):
        index_val = letters.index(decoded[i]) + int(key)
        word += letters[index_val]
    
    counter = 0
    line_counter = 0
    for i in range(len(msg)):
        counter += 1
        if counter == 6:
            word = word[:i] + " " + word[i:]
            counter = 0
            line_counter += 1
            if line_counter == 10:
                word = word[:i] + "\n" + word[i:]
                line_counter = 0
                counter -= 1
    
    print(word)