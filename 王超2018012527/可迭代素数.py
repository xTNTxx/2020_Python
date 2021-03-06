def isPrimeNum(k):
    if k < 2:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for k in range(self.start, self.end):
            if self.isPrimeNum(k):
                yield k

    def isPrimeNum(self, k):
        pass


for x in PrimeNumbers(1, 10000):
    print(x)
