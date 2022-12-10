def printcontentslist(L):
    for x in L:
        if x%2==0:
            print("Even")
        else:
            print("odd")
        if x==10:
            print("Ten")
        elif x==20:
            print("twenty")
        elif x==30:
            print("thirty")
        elif x==40:
            print("forty")
        else:
            print("fifty")
def print_ok(L):
    s = 1
    for i in L:
        s = s*i
        print(s)
        l1 = [1,2,3,4,5]
        print_ok(1)
        print(x,end=' ')
l1 = [10,20,30,40,50]
printcontentslist(l1)
print(len(l1))

