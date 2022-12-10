#1
l1 = [1,2,3]
l2 = l1 * 3
print(l2)
#2
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

#3
l1 = [1,2,3,'a','b','c']
print(30 in l1)
print(3 in l1)

#4
A = 'hello'
B = 'hello'
print(A is B)
A = 'hello'
B = 'helo'
print(A is B)

#5
l1 = [100,200,300]
del l1[0]
print(l1)

#6
l1 = [10,20,30]
del l1[-3]
print(l1)
