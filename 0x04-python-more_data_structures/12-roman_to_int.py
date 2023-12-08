#!/usr/bin/python3
def roman_to_int(s:"str")->"int":
    number = 0
    roman = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    return number + roman[s[-1]]
