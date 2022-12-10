#area#circle#rectangle
class area():
    def __init__(self,pi):
        self.pi=pi
    def area_circle(self):
        r = int(input("enter the radius: "))
        print("area of circle: ",self.pi*r**2)
    def area_rectangle(circle):

        l = int(input("ENTER THE 1st SIDE:"))
        b= int(input("ENTER THE 2nd SIDE:"))
        print("AREA OF RECTANGLE IS : ",l*b)
p1 = area(3.14)
p1.area_circle()
p1.area_rectangle()
    
