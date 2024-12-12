def compute_word_frequency(text:str):
    words = sorted(text.split(' '))
    count = {}
    for word in words:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1
    output = ""
    for word,freq in count.items():
        output += f"{word}:{freq} "
    return output

print(compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))