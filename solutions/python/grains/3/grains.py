def square(number):
    """
    number(int): must be a number between 1 and 64 both inclusive
    This function receives number and finds the number of grains on a 
    given square on a chessboard

"""
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    add = 0
    for digit in range(1, 65):
        add += square(digit)
    return add

