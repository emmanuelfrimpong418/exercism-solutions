def square(number):
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    add = 0
    for digit in range(1, 65):
        add += square(digit)
    return add

