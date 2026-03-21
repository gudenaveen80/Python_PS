import types
class Vehicle:
    
#     def info(self,name,color,model):
#         self.name=name
#         self.color=color
#         self.model=model
# benz = Vehicle()
# benz.info('benz','white','benz143')
# print(benz.color,benz.model,benz.name)

    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand
    def milleage(self):
        print('gives 50 kmph')
benz1 = Vehicle('benz','black','benz123')
print(benz1.name,benz1.color,benz1.brand)

benz1.milleage=types.MethodType(milleage,benz1)



class Dad:
    def __init__(self):
        print('dad i love you')
    def eat(self):
        print('he loves food')
        
class Child(Dad):
    def __init__(self):
        super().eat()
        print('he sleeps always')
p1 = Dad()

p2=Child()



class Vehicle:
    def veh_info(self):
        print('this is vehicle info')
        
class Car(Vehicle):
    def Car_info(self):
        print('this is car info man')
class Van(Vehicle):
    def Van_info(self):
        print('this is school van')
class Ecos(Car,Van):
    def Ecos_info(self):
        print('this is 10 seater car')
v1 = Van()
v1.veh_info()
v2 = Ecos()
v2.veh_info()

v2.Van_info()
v2.Car_info()


class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
        
cal1 = Calculator()

print(cal1.add(2,3))
print(cal1.add(2,3,4))




# str1 = input("enter string:")
# count=0
# for i in str1:
#     count+=1
#     print(f'{i}{count}',end=' ')

class Company:
    def __init__(self,cmp_name,est_year):
        self.company=cmp_name
        self.year=est_year
class Employee(Company):
    def __init__(self,name,salary,company):
        self.name=name
        self.__salary=salary
        self._company=company
    def salary_details(self):
        print(self.__salary)
e1 = Employee("naveen",100000,'tcs')
print(e1.name)
e1.salary_details()
print(e1._company)


class Minus:
    @staticmethod
    def sub(x,y):
        return x-y
print(Minus.sub(20,10))

s1 = Minus()
print(s1.sub(50,30))

class College:
    college_name='rk valley'
    uniform = 'blue'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(cls,college_name):
        cls.clg_name=college_name
S1 = College('naveen',22)
print(S1.college_name)
S1.college_name='ongole'
print(S1.college_name)
S2 = College('anusha',22)


College.college_name='ongole campus'
print(S2.college_name)
print(S2.college_name)


class Vector:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        print(self.x+other.x,self.y+other.y)
        
v1 = Vector(10,20)

v2 = Vector(20,30)


print(v1+v2)

class Employee:
    def __init__(self,salary):
        self._salary=salary
        
    def get_salary(self):
        return self._salary
    def set_salary(self,value):
        if value>0:
            return self._salary
        else:
            print('salary is positive')
e1 = Employee(100000)
e1.set_salary(40000)
print(e1.get_salary())


list1 = [1,2,3,4]

hi = iter(list1)

print(hi.__next__())
print(hi.__next__())
print(hi.__next__())

