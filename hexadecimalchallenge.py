hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
        
    exponent = 0
    decimalValue = 0

    for char in hexNum[::-1]:
        decimalValue += hexNumbers[char] * (16 ** exponent)
        exponent += 1
    return decimalValue

print(hexToDec('123444'))
