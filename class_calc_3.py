class Person:
    def __init__(ram, name, age):
        ram.name = name
        ram.age = age

    def myfunc(ram):
        print("Hello my name is ",ram.name)
        print("Age = ",ram.age)


p1 = Person("John", 36)
p1.myfunc()
