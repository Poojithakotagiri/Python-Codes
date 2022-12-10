d = { }
print(type(d))

D = {'virat kohli':52,'sachin':100}
print(D)
D['Dhoni']=28
print(D)
del D['Dhoni']
print(D)

R = {'shakti' : 66,'poojitha':65,'abhinash' : 64,'dhruv' : 63,'shiva':62, 'dinesh':61}
print(R['shakti'])
print(R['poojitha'])
print(R['abhinash'])
print(R['dhruv'])
print(R['shiva'])
print(R['dinesh'])

D = {'virat kohli':52,'sachin':100,'Dhoni':28}
for key in D:
    print('centuries scored by ',key,'=',D[key])

RN = {'shakti' : 66,'poojitha':65,'abhinash' : 64,'dhruv' : 63,'shiva':62, 'dinesh':61}
for key in RN:
    print('student',key,'=',RN[key])
    
car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.keys()

print(x) 

car["color"] = "white"

print(x) 

car = {"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

