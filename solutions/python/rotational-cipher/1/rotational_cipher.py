import string

def rotate(text, key):
    new_text = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    n = int(key)
    for letter in text:
        if letter in lower:
            index = lower.index(letter)
            new_text += lower[(n + index) % 26]
        elif letter in upper:
            index = upper.index(letter)
            new_text += upper[(n + index) % 26]
        else:
            new_text += letter
    return new_text