def is_armstrong_number(number):
    total = 0
    value = str(number)
    for digit in value:
        total += int(digit) ** len(value)
    return total == number