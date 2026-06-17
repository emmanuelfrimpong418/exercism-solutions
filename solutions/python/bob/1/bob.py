def response(hey_bob):
    if hey_bob.strip() == "":
        answer = "Fine. Be that way!"
    elif hey_bob.strip().endswith("?") and hey_bob.isupper():
        answer = "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith("?"):
        answer = "Sure."
    elif hey_bob.isupper():
        answer = "Whoa, chill out!"
    else:
        answer = "Whatever."
    return answer
