#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    prev_value = 0
    for numeral in roman_string:
        if numeral not in rom_val:
            return 0
        value = rom_val[numeral]
        if value > prev_value:
            int_num += value - 2 * prev_value
        else:
            int_num += value
        prev_value = value
    return int_num
