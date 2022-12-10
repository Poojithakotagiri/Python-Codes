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
        self.admnyear = admnyear
        self.branch = branch
        student.__init__(self,name,enrollnumber)
obj = college("shakti",1220709,2022,"cse")
obj.display()
