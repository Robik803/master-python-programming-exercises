def divisible_binary(seq:str):
    b_nums = seq.split(',')
    nums = []
    for x in b_nums:
        num = 0
        for i in range(4):
            num += int(x[i])*2**i
        if num%5 == 0:
            nums.append(x)
    return ','.join(nums)