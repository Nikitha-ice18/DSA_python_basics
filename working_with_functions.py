#defing a function

def my_function():
    print("Hello from a function")

### changing temperature from celsius to fahrenheit using function
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(fahrenheit_to_celsius(77))  
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(100))

###Argurments and Parameters

def greet(name):   #name is a parameter
    print("Hello, " + name + "!")
    print("Welcome to the world of functions.")

greet("Nikki")  #nikki is an argument 
greet("Deekshi")
greet("yashu")



##default parameter value
def my_function(name = "friend"):
    print("Hello",name)

my_function("Nikki")
my_function()    #if the function is called without an argument, it uses the default value

def student_info(name="student"):
    print("I am ",name)

student_info("Nikki")
student_info()  #if the function is called without an argument, it uses the default value


## keyword arguments

def my_function(animal,name):
    print("I have a",animal)
    print("My", animal +"'s name is", name)

my_function(animal="Dog", name="Nikki")
