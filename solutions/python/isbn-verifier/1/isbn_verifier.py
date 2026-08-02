def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    n = 10
    for char in isbn:
        if char == "X" and n == 1:
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += value * n
        n -= 1
    return total % 11 == 0
