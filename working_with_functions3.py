### *args and **kwargs

def my_func(*kids):
    print("the youngest child is " + kids[0])

my_func("Emil", "Tobias", "Linus")


def my_func2(*args):
    print("Type:", type(args))
    print("first argument:", args[0])
    print("second argument:",args[1])
    print("all arguments;",args)

my_func2("nikki","kushi","hema","gova","sai")

#using *args with regular arguments

def my_func3(greeting, *names):
    for name in names:
        print(greeting, name)

my_func3("Hello", "person1","person2","person3")


# *args is useful when you want to create flexible functions

def my_func4(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_func4(1,2,3,4,5))
print(my_func4(10,20,30))
print(my_func4(5))

#finding max num 

def my_func5(*numbers):
    if len(numbers)==0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num>max_num:
            max_num = num

    return max_num

print(my_func5(1,2,3,4,5,67))


###  Arbitrary Keyword Arguments **kwargs

def my_func6(**kid):
    print("his last name is " +kid["lname"])

my_func6(fname = "nikki",lname="bandaru")


#accessing values from **kwargs

def my_func7(**myvar):
    print("Type:",type(myvar))
    print("Name:",myvar["name"])
    print("Age:",myvar["age"])
    print("All data:",myvar)

my_func7(name = "Nikitha", age= 19, city="newyork")

# you can combine regular parametes with **kwargs

def my_func8(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ",key +":", value)

my_func8("nikki121212",age=29,city="newyork",hobby="coding")

#we can also use *args and **kwargs together in a function

#the order must be:
# 1.regular parameters
# 2. *args
# 3. **kwargs

def my_func9(name, *args, **kwargs):
    print("Name:", name)
    print("positional arguments:", args)
    print("Keyword arguments:", kwargs) 

my_func9("User info","nikki","tonias",age=23,city="oslo")

### Unpacking arguments
# unpacking lists wit *

def my_func10(a,b,c):
    return a+b+c

numbers = [1,3,4]
result = my_func10(*numbers)
print(result)

# unpacking dictionaries with **

def my_func11(fname, lname):
    print("hello", fname,lname)

person ={"fname":"nikki","lname":"bandaru"}
my_func11(**person)
    