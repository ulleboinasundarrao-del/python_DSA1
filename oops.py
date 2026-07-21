# class A:
#     def __init__(self,name,age,gender):
#         self._age=age
#         self.gender=gender
#     def display(self):
#         print(self.__name)
#         print(self.__age)
#         print(self,age)   
# a1=A("sriram",21,"male")
# a2=A("divya",21,"female")
# print(a1.__name)
# print(a2.__age)
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balence+=amount
    def withdraw(self,amount):
        self.__balence-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class savingAccount(BankAccount):
    def interestcalc(self):
        interest = self.getBalance() * 0.05
        return interest
#polymorphism:
class Animal:
    print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("woof")
class Cat(Animal):
    def sound(self):
        print("meow")            
