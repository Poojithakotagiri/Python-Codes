#1
import random
print(random.randint(0,100))
#2
a = 100
for i in range(1,a+1):
    print(i)
#3
for i in range(0,2):
    for j in  range(0,2):
        print(i,j)
    print("\n")
#4
    
rows=4                              #1
for row in range(1,rows+1):         #12
    for coloumn in range(1,row+1):  #123
        print(coloumn,end=" ")      #1234
    print(" ")

    
#5
rows = 5
for num in range(rows):
    for i in range(num):
        print(num,end=" ")
    print(" ")
#6
def fact(m):
    if(m==1):
        return(1)
    else:
        return(m*fact(m));
n=int(input("enter the no"))
f=fact(n)
print("Factorial of a no =",f)
print("")    


