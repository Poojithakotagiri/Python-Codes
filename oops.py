class calc:
    def sum(self):
        a = int(input("Enter no.: "))
        b = int(input("Enter a second no.: "))
        c = a+b
        print("sum=",c)
    def sub(self,m,n):
         o = m-n
         print("sub=",o)
    def multi(self,m,n):
        o=m*n
        return o;

f = calc()
f.sum()
f.sub(20,10)
o = f.multi(10,20)
print("multiplication=",o)
        
