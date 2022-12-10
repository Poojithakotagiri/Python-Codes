try:
    a = int(input("1st number;"))
    b = int(input("2nd number:"))
    print(a/b)
except ZeroDivisionError:
    print("mat kar divide zero")
except TypeError:
    print("unsupported operation")
except ValueError:
    print("value error Unsupported operation")
print("out  of try except blocks")


def Add(x, y):
    while (y != 0):
        carry = x & y 
        x = x ^ y
        y = carry << 1
    return x
print(Add(27,5))


