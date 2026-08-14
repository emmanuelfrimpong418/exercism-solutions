def is_pangram(sentence):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
        
        
