#1
def sum():
    a=7
    b=8
    c=a+b
    print("sum=",c)
print("outside function")
sum()
print("BYE HAVE A GREAT TIME")
print("\n")

#2
def sum(a,b):
    c=a+b
    print("sum=",c)
print("outside function")
m=7
n=8
sum(m,n)
sum(10,15)
print("BYE HAVE A GREAT TIME")
print("\n")

#3
def sum(a,b):
    c=a+b
    print("sum inside ")
    return c;
print("outside function")
m=7
n=8
o=sum(m,n)
print("sum=",o)
print("BYE HAVE A GREAT TIME")
print("\n")

#4
def sum(a,b):
    c=a+b
    return c;
def sub(m,n):
        z=m-n
    return z;
def multi(i,j):
    k=i*j
    return k;
print("outside the function")
d=sum(7,8)
print("sum=",d)
f=sub(20,5)
print("sub=",f)
g=multi(7,9)
print("multi=",g)
print("BYE HAVE A GREAT TIME")
print("\n")

