#Decorators : Let you add extra behavior to a function, without changiing the functions's code
#A deccorator us a function that takes another function as input and returns a new function

#Basic decorator

def change_case(func):  # defining a decorator function that takes another function as an argument
    def myinner():                # defining an inner function that will replace the original function
        return func().upper()    # Convert the result of the original function to uppercase
    return myinner              # Return the modified function

@change_case                    # Using the decorator to modify the behavior of my_function
def my_function():        # defining the original function
    return "Hello niKkI"    # Return a string with mixed case

print(my_function())  # Output: HELLO NIKKI   


# Multiple Decorator calls
#a decorator can be called mutliple times.Just the decorator above the function you want to decorate.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello world"

@changecase 
def otherfunction():
    return "I am magic"

print(myfunction())
print(otherfunction())

#Arguments in the decorated function

#functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function

def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(name):
    return "Hello "+ name

print(myfunction("nikki"))

# *args and *kwargs
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, *kwargs).upper()
    return myinner

@changecase
def myfunction(name):
    return "hello "+ name

print(myfunction("kushika"))

#decorator with arguments

#decorator can accept their own arguments by adding another wrapper level

def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(1)
def myfunction():
    return "Hello hema"

print(myfunction())

#multiple decorators

#decorators are called in the reverse order, starting with the one closet to the function

#example : one decorator for upper case and one for adding a greeting

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "hello "  + func() + " have a good day!"
    return myinner

@changecase
@addgreeting
def myfunc():
    return "govardhana"

print(myfunc())

