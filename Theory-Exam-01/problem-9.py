'''---------------------------------------------------------------------------------
9. Write a class with two instance variables X, n . Add two methods sum() and pow() 
to get the sum (X+n) and exponential/power of X^n .
-------------------------------------------------------------------------------------'''

class mathmatics:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        return self.X+self.n
    
    def pow(self):
        i = self.n
        exp = 1
        while(i):
            exp = exp*self.X
            i = i-1
        
        return exp
    
a = mathmatics(2, 3)

print(a.sum())
print(a.pow())




