def all_digits_even():
    even = []
    for i in range(1000,3001):
        dig = str(i)
        if int(dig[0])%2 == 0 and int(dig[1])%2 == 0 and int(dig[2])%2 == 0 and int(dig[3])%2 == 0:
            even.append(dig)
    return ','.join(even)

print(all_digits_even())