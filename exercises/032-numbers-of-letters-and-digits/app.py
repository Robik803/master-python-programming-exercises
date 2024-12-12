def letters_and_digits(seq):
    count = {"LETTERS":0,"DIGITS":0}
    for l in seq:
        if l.isdigit():
            count["DIGITS"] += 1
        elif l.isalpha():
            count["LETTERS"] += 1
    return f"LETTERS {count['LETTERS']} DIGITS {count['DIGITS']}"

print(letters_and_digits("hello world! 123"))