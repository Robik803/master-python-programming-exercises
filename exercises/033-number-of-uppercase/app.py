def number_of_uppercase(seq):
    count = {"UPPERCASE":0,"LOWERCASE":0}
    for l in seq:
        if l.isupper():
            count["UPPERCASE"] += 1
        elif l.islower():
            count["LOWERCASE"] += 1
    return f"UPPERCASE {count['UPPERCASE']} LOWERCASE {count['LOWERCASE']}"

print(number_of_uppercase("Hello world!"))
