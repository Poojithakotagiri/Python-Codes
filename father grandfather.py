class grandfather:
    def __init__(ram, name, age):
        ram.name = name
        ram.age = age
    def grandfatherdetail(ram):
        print("Hello my name is ",ram.name)
        print("Age = ",ram.age)
class father(grandfather):
    def __init__(satya,name,age):
        satya.name=name
        satya.age=age
    def fatherdetail(satya):
        print("hello my name is", satya.name)
        print("age=",satya.age)
class son(father,grandfather):
    def __init__(shakti,name,age):
        shakti.name=name
        shakti.age=age
    def sondetail(shakti):
        print("hello people")
        print("my name is ",shakti.name)
        print("age=",shakti.age)


p1 = grandfather("ram",73)
p1.grandfatherdetail()
p1=father("satya",56)
p1.fatherdetail()
p1=son("shakti",19)
p1.sondetail()
