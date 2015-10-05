def anti_vowel(text):
    new = ""
    for i in range(0,len(text)):
        if text[i] in "aeiouAEIOU":
            i += 1
        else:
            new = new + text[i]
    return new
