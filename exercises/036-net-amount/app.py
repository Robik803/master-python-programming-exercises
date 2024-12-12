def net_amount(seq):
    transactions = seq.split(' ')
    net = 0
    assert len(transactions)%2 == 0
    for i in range(len(transactions)//2):
        if transactions[2*i] == 'D':
            net += int(transactions[2*i+1])
        elif transactions[2*i] == 'W':
            net -= int(transactions[2*i+1])
    return net