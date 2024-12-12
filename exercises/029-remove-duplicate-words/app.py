def remove_duplicate_words(seq:str):
    return" ".join(sorted(set(seq.split(' '))))