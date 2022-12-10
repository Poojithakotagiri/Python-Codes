class calc:
    def sum(self):
        a=int(input("Enter 1st no. "))
        b=int(input("enter 2nd no. "))
        c=a+b
        print("sum=",c)
    def sub(self,a,b):
        c=a-b
        print("sub=",c)
    def multi(self,m,n):
        z=m*n
        return z;

f1 = calc()
f1.sum()
f1.sub (10,20)
i = int(input("enter 1st no.: "))
j = int(input("enter 2st no.: "))
k = f1.multi(i,j)
print("multi=",k)
f2=calc()
f2.sum()
f2.sub(7,8)
l=f2.multi(10,20)
print("multiplication=",l)


