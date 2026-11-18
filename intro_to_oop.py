# OOP is a programming paradigm that uses "objects" to design applications and computer programs. OOP allows for modeling real-world scenerios using
#classes and objects.
#Basics of OOP
#A class is a blue print for creating objects,attributes,methods.
class Car:
    pass

audi=Car()
bmw=Car()

print(type(audi))
print(audi)   #gives the specific location

#instance variables and methods
audi.windows=4
tata=Car()
tata.doors=4
#print(tata.windows)  #gives error because not clear attributes
print(audi.windows)

# __init__ method called as constructor
class Dog:
    def __init__(self,name,age): #self keyword is resposible in probably accessing the instance variable inside the class itself.
        #constructor
        self.name=name
        self.age=age
#create objects
dog1=Dog("ricky",4)
dog2=Dog("luci",5)
dog3=Dog("july",3)
print(dog1)
print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog3.name)

#defining a class with instance methods

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(f"{self.name} says moew moew")
    def aging(self):
        print(f"{self.name} is {self.age} year old")
    

cat1=Cat("katie",3)
cat1.bark()
cat1.aging()

#modelling a bank account
#define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!!!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

    def get_balance(self):
        print(f"available balance is {self.balance}")

##create an object

account=BankAccount("Nikitha",5000)
print(account.balance)

#call instance methods
account.deposit(100)

account.withdraw(300)

account.get_balance()





     



