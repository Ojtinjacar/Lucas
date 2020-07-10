
class FibonacciCode:

    def __init__(self):
        self.l_0 = 2
        self.l_1 = 1

    def numLucas(self, n):
        if n  == 0:
            return self.l_0
        elif n == 1:
            return self.l_1
        else:
            return self.numLucas(int(n-1))+ self.numLucas(int(n-2))



a = FibonacciCode()
print(a.numLucas(9))
