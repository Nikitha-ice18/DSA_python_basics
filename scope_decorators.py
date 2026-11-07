#scope
#A variable is only available from inside the region it is created.This is called scope.

#local scope: A variable created inside a function belongs to the local scope if that fucntion, and can only be used inside the functions.

#example
def my_func():
    x=300
    print(x)

my_func()

#function inside function
def my_func1():
    x=300
    def my_innerfunc():
        print(x)

my_func1()

#Global scope

# A variable created in the main body of the python code is a global variable and belongd to the global scope

x=300

def myfunc():
    print(x)

myfunc()
print(x)

x=300         #global
def my_func2():
    x=200
    print(x)

my_func2()

print(x)

#global keyword
 
#If you need to create a global variable, but stuck in the local scope, you can use the global keyword

def my_func3():
    global x
    x=300

my_func3()
print(x)

#to change the global variable inside a function 

x=300
def my_func4():
    global x
    x=200

my_func4()
print(x)   #now the output will be 200 instead of 300 because we changed the value of the global variable x inside the function my_func4() using the global keyword.

#non local keyword : used to work with variables inside nested functions, where the variable should not belong to the inner function.

def my_func5():
    x="Mike"
    def my_innerfunc():
        nonlocal x
        x="hola"
    my_innerfunc()
    return x

print(my_func5())  #output will be "hola" instead of "Mike" because we changed the value of the variable x inside the inner function my_innerfunc() using the nonlocal keyword.  

#another example

x="global"     #set a global variable

def outer():
    x ="enclosing"   #change the value of the variable x inside the outer function outer()
    def innner():
        x="local"     #change the value of the variable x inside the inner function inner()
        print("Inner:",x)
    innner()
    print("Outer:", x)

outer()
print("Global:",x)