from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result
    else:
        return sub(a, b)
