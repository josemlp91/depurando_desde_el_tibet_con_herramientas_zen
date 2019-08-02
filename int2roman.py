#!/usr/bin/env python

def int2roman(number):
    breakpoint()

    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )

    if number <= 0 or number >= 4000 or int(number) != number:
        raise ValueError('Input should be an integer between 1 and 3999')

    result = []
    for integer, roman in coding:
        while number >= integer:
            result.append(roman)
            number -= integer
    return ''.join(result)
