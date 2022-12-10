a = int(input("enter a number A = "))
b = int(input("enter a number B = "))
c = int(input("enter a number C = "))
d = int(input("enter a number D = "))
if(a>b):
    if(a>c):
        if(a>d):
              print("a is big")
        else:
            print("d is big")
    else:
         if(c>d):
                print("c is big")
         else:
             print("d is big")
else:
    if(b>c):
        if(b>d):
            print("b is the greatest")
        else:
            print("d is the greatest")
    else:
        if(c>d):
            print("c is the greatest")
        else:
            print("d is the greatest")
print("bye have a great time")
