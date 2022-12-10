# constructor of parent class
class student:
    def __init__(self,name,enrollnumber):
        self.name = name
        self.enrollnumber = enrollnumber
    def display(self):
        print(self.name)
        print(self.enrollnumber)
#child class
class college(student):
    def __init__(self,name,enrollnumber,admnyear,branch):
        self.name = name
        self.enrollnumber = enrollnumber
        self.admnyear = admnyear
        self.branch = branch

    def display(self):
        print(self.admnyear)                                            #function overriding
        print(self.branch)
        print(self.enrollnumber)
        print(self.name)
#creation of an object for base/derived class
obj = college("shakti",12205709,2022,"cse")
obj.display()



