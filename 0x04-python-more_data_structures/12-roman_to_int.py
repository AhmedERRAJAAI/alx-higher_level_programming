#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(romain_string) != str or not romain_string:
        return 0

    roman_digit_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    last_digit_value = 0

    if isinstance(roman_numeral, str) and roman_numeral:
        for symbol in reversed(roman_numeral):
            current_digit_value = roman_digit_map[symbol]
            if current_digit_value >= last_digit_value:
                integer_value += current_digit_value
            else:
                integer_value -= current_digit_value
            last_digit_value = current_digit_value
    return integer_value

