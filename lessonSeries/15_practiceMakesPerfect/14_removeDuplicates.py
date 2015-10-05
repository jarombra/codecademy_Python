def remove_duplicates(words):
    removed = [ ]
    for w in words:
        if w not in removed:
            removed.append(w)
    return removed
