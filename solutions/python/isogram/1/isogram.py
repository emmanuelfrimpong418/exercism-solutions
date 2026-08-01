def is_isogram(word):
    letters = [char for char in word.lower() if char.isalpha()]
    return len(letters) == len(set(letters))