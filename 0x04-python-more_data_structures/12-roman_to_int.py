#!/usr/bin/python3

def calculate_difference(values):
    total = sum(values)
    maximum = max(values)
    return maximum - (total - maximum)

def roman_to_integer(roman_numeral):
    if not isinstance(roman_numeral, str) or not roman_numeral:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    current_group = []
    previous_value = 0

    for char in roman_numeral:
        if char not in roman_values:
            return 0  # Invalid Roman numeral character
        
        current_value = roman_values[char]
        
        if current_value <= previous_value:
            result += calculate_difference(current_group)
            current_group = [current_value]
        else:
            current_group.append(current_value)
        
        previous_value = current_value

    result += calculate_difference(current_group)
    return result
