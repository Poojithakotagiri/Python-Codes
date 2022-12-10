#factorial#
#case1#
print("WITH FOR LOOP")
n = int(input("enter the no"))
f = 1
if (n == 0):
    print("factorial of a no =", 1)
else:
    for i in range(1, n+1):
        f = f*i
    print("factorial of a no", f)
print("")

#2#
print("WITH WHILE LOOP")
a = int(input("enter the no : "))
f = 1
i = 1
while (i <= a):
    f = f*i
    i = i+1
print("factorial of the no : ", f)
print("")

#case3#
n = int(input("enter the no"))


def fact(m):
    f = 1
    if (m == 0):
        print("factorial of a no =", 1)
    else:
        for i in range(1, m+1):
            f = f*i
        print("factorial of a no", f)


fact(n)
fact(6)
print("")


return (m*fact(m1))
return (5*fact(4))
(5*4*fact(3))
(5*4*3*fact(2))
(5*4*3*2*fact(1))
(5*4*3*2*1)
return (f)
o = fact(n)
print("factorial of a no=", o)
p = fact(6)
print("Factorial of a no=", p)

#case5#


def fact(m):
    if (m == 1):
        return (1)
    else:
        return (m*fact(m))


n = int(input("enter the no"))
f = fact(n)
print("Factorial of a no =", f)
print("")

#case6#


def fact():
    f = 1
    if (n == 0):
        print("factorial", 1)
    else:
        for i in range(1, n+1):
            f = i*f
    print("factorial of a no : ", f)


fact()
