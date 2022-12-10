#1 (no return no argument)
def sum():
    a=1
    b=2
    c=a+b
    print("sum",c)
sum()

#2(no return yes argument)
def sub(a,b):
    c=a-b
    print("sub= ",c)
d=int(input("enter your number: "))

e=int(input("enter your number: "))
sub(d,e)

#3 (yes argumennt yes return)
def multi(a,b):
    c=a*b
    print("product = ",c)
    return c;
m=int(input("enter the number : "))
n=int(input("enter the 2nd number : "))
multi(m,n)

#4(yes return no argument)
def div():
   a=15
   b=5
   c=a/b
   print("result is : ",c)
   return c;
div()
print("BYE VYE")

