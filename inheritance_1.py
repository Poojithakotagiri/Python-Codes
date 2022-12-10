#single inheritance
#base class
class parent:
    def func1(self):
        print("This function is in parent class.")
#Derived class
class child(parent):
    def func2(self):
        print("This is  function is in child class.")
#Driver's code
object = child()
object.func1()
object.func2()


#multiple inheritance
#base class
class first:
    def func1(self):
        print("this fun is from first class")
class second:
    def func2(self):
        print("this fun is from second class")
class third(first,second):
    def func3(self):
        print("this fun is from third class")
#driver's code
o=third()
o.func1()
o.func2()
o.func3()


#
class person(object):
    #constructor
    def __init__(self,name, id):
        self.name = name
        self.id = id
    #to check if the person is an employee
    def Display(self):
        print(self.name,self.id)

#drivers code
emp = person("satyam",102)#AN object of a person
emp.Display()
