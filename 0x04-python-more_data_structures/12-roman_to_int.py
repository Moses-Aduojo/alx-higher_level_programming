#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
        'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
        'CM': 900, 'M': 1000
    }

    numeral_list = []
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in numerals:
            numeral_list.append(roman_string[i:i+2])
            i += 2
        else:
            numeral_list.append(roman_string[i])
            i += 1

    _sum = 0
    for item in numeral_list:
        if item in numerals:
            _sum += numerals[item]
        else:
            return 0

    return _sum
