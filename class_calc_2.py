class calc:
    def __init__(self,m,n):
        self.a=m
        self.b=n
    def sum(self):
        c = self.a+self.b
        print("sum=",c)
    def sub(self):
        d = self.a-self.b
        print("sub=",d)
    def multi(self):
        e = self.a*self.b
        return e;
f1 = calc(10,20)
f1.sum()
f1.sub()
z=f1.multi()
print("mult=",z)
m = int(input("enter 1st number: "))
n = int(input("enter 2nd number: "))
f2=calc(m,n)
f2.sum()
f2.sub()
o = f2.multi()
print("multi=",o)

