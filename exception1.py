def enterage(age):
    if age < 0:
        raise ValueError("only positive intergers are allowed")
    if age % 2 ==0:
        print("age is even")
try:
    num = int(input("Enter your age : "))
    enterage(num)
except ValueError:
    print("Only +ve intergers are allowed")
except:
    print("something is wrong")
