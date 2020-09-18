from bisect import bisect_left

class BinSearchFxn:
    def __init__(self):
        self.fxn = lambda n: n*(n+1)//2
        self.uppbound = 10**18
    def __getitem__(self,i):
        return self.fxn(i)
    def __len__(self):
        return self.uppbound

a = BinSearchFxn()
insertion = bisect_left(a, 10**18 - 1000)
print(insertion)
