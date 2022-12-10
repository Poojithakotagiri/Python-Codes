#1(for loop)
n=int(input("enter a no."))
f = 1
if(n==0):
      print("factorial of a no. is ",1)
else:
    for i in range (1,n+1):
        f=f*i

print("factorial of a no. is =",f)

#2
n=int(input("enter a number:"))
def fact(m):
    f=1
    if(m==0):
        print("factorial of a no. is = ",1)
    else:
        for i in range(1,m+1):
            f=f*i
        print("factorial of a no. is = ",f)
fact(n)
fact(6)

#3(with while loop)
a=int(input("enter the number : "))
f=1
i=1
while(i<=a):
    f=f*i
    i=i+1
print("factorial of the number is = ",f)
print(" ")
