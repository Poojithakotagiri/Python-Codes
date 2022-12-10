t1 = ()
t2 = (12,13,14,15,56,90,67)
t3 = ('a','b','c','d','e')
t4 = 1,2,3,4
print(t1)
print(t2)
print(t3)
print(t4)
#4the + and * operator
a = ('a','b')
b = (1,2)
c = a+b
print(type(a+b))
print(c)
#* operator
t = (1,2,3)
t1 = t*2
print(t1)
#sorting  elements of tuple
t = (56,45,32,25)#tuple
t = list(t)#converted tuple to a list
t.sort()#sort method of list
print(tuple(t))
