x = lambda a : a + 10
print(x(100000))
#2 variable
x = lambda a,b : a*b
print(x(5,6))
#3 
max = lambda a,b : a if(a>b) else b
print(max(1,2))
#4
ages = [12,13,16,19,27,35,9]
adults = list(filter(lambda age: age >18,ages))
print(adults)
