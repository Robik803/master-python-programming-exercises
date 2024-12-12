def list_and_tuple(*t):
    return [str(x) for x in t], tuple(str(x) for x in t)

print(list_and_tuple(34,67,55,33,12,98))