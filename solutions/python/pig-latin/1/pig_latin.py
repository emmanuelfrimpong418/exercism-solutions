vowels = ["a", "e", "i", "o", "u"]

def translate(text):
    new_text = []
    words = text.split(" ")
    for word in words:
        if word[0] in vowels or word.startswith(("xr", "yt")):
            new_text.append(start_vowel(word))
        else:
            new_text.append(start_consonant(word))
    return " ".join(new_text)



def start_vowel(text):
    if text[0] in vowels or text.startswith(("xr", "yt")):
        text += "ay"
    return text

def find_cluster_end(word):
    i = 0
    while i < len(word):
        if word[i] in vowels or (word[i] == "y" and not word.startswith("y")):
            break
        if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
            i += 2
        else:
            i += 1
    return i

def start_consonant(text):
    i = find_cluster_end(text)
    prev = text[:i]
    after = text[i:]
    new_text = after + prev
    new_text += "ay"
    return new_text




