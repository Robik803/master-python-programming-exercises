class DivisibleIterator7:
    
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        for i in range(0,self.n+1,7):
            yield i

iterator = DivisibleIterator7(26)

for i in iterator:
    print(i)