# method overriding

# Defining parent class

class Parent():

# Constructor

    def __init__(self): self.value = "Inside Parent"

# Parent's show method def show(self): print(self.value)

# Defining child class class Child(Parent):

# Constructor

def _init_(self): self.value = "Inside Child"

# Child's show method def show(self): print(self.value)

# Driver's code

obj1 = Parent()

obj2 = Child()
