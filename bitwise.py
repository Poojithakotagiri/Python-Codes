a = 60       #60 = 0011 1100
b = 13       #13 = 0000 1101
c = 0

c = a & b;      #12 = 0000 1100
print("line 1 - value of c is " , c)
c = a | b;       #61 = 0011  1101
print("line 2 - value of c is " , c)
c = a ^ b;       #49 = 0011 0001
print("line 3 - value of c is ", c)
c = ~a;          #-61 = 1100 0011
print("line 4 - value of c is ", c)
c = a<<2;        #240 = 1111 0000
print("line 5  - value of c is ", c)
c = a>>2;        #15 = 0000 1111s
print("line 6 - value of c is ", c)
