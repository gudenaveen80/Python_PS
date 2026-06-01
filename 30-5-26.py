class Parent:
    def show (self):
        print('this is parent class')

class Child(Parent):
    def show(self):
        super().show()
        print('this is child class')
        
c1 = Child()
c1.show()

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(3000)
print(account.get_balance())



from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Lion(Animal):
    def sound(self):
       return 'roar'
       
class Tiger(Animal):
    def sound(self):
       return 'again roar'
a1 = Lion()
a2 = Tiger()
print(a1.sound())
print(a2.sound())