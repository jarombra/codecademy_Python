def reverse(text):
    text_array = []

    for c in text:
        text_array.insert(0, c)
    return ''.join(text_array)
    
# Or...

def reverse(text):
    txet=""
    length = len(text) - 1

    while length >= 0:
        txet += "%s"%text[length]
        length -= 1
    return txet
    
# Or...

def reverse(text):
    new_text = ""
    length = len(text)
    for letter in text:
        last_letter = text[length -1]
        new_text += last_letter
        length -= 1
    return new_text
