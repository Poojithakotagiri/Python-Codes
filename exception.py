try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("Division error by zero is error!!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
except:
    print("wrong input")
else:
    print("No exception")
finally:
    print("This will execute")
    
