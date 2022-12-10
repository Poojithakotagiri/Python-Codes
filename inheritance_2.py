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
