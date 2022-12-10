###
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        n = self.a+self.b
        print("sum=",n)
    def sub(self):
        m = self.a-self.b
        print("sub=",m)
    def multi(self):
        o = self.a*self.b
        print("multi=",o)
p1 = calc(2,3)
p1.sum()
p1.sub()
p1.multi()
m=int(input("enter a no."))
n=int(input("enter a no."))
p2=calc(m,n)
p2.sum()
p2.multi()
#
class area():
    def __init__(self,pi):
        self.pi=pi
    def area_circle(self):
        r = int(input("enter the radius: "))
        print("area of circle: ",self.pi*r**2)
p1 = area(3.14)
p1.area_circle()
#
class account:
    def f1(self,a,b):
        self.accno=a
        self.balance=b
acc1=account()
acc1.f1(200,6000)
print(account.__dict__)
    
