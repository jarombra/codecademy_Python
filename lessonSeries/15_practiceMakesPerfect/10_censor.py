def censor(text, word):
    length = len(word)
    text = text.split()
    x = 0
    while len(text) > x:
        if text[x] == word:
            text[x] = "*" * length
            x = x + 1
    return " ".join(text)

# Or...

def censor(text, word):
    wordlist = text.split()
    replace = "*" * len(word)
    for i, x in enumerate(wordlist):
        if x == word:
            wordlist[i] = replace
    return " ".join(wordlist)
