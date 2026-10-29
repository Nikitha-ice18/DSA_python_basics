##postional arguments

def my_func(friend,name):
    print("I have a",friend)
    print("My",friend +"'s name is", name)

my_func("bestie","sai")

#mixed positional and keyword arugments

def my_function(animal,name,age):
    print("I have a",age,"year old", animal,"named",name)

my_function("dog","nikki",8)

#sending list as an argument
def my_fruits(fruits):
    for fruit in fruits:
        print("I like",fruit)

my_fruitees=["apple","banana","grapes","mango"]
my_fruits(my_fruitees)

#sending dictionary as an argument

def my_func2(person):
    print("Name:",person["name"])
    print("Age:",person["age"])

my_func1={"name":"sai","age":20}
my_func2(my_func1)

#postional only arguments
def my_pos(name, /):
    print("Hello", name)

my_pos("nikki")

#keyword only arguments

def my_func3(*, name):
    print("hello",name)

my_func3(name = "Nikki")

### args and kwargs

#if you do not know how many arguments will be passed into your fucntion, add a * before 
#the parameter name.

def my_func4(*kids):
    print("The youngest child is "+kids[2])

my_func4("nikki","hema","gova")


#another example
def my_func5(greeting,*names):
    for name in names:
        print(greeting,name)

my_func5("hello","nikki","hema","sai")

# 
def my_func6(*numbers):
    total =0
    for num in numbers:
        total +=num
    return total


print(my_func6(1,2,3))
print(my_func6(10,20,30,40,50))
print(my_func6(5))

#finding the maximum value

def my_func7(*numbers):
    if len(numbers)==0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num>max_num:
            max_num = num
    return max_num

print(my_func7(3,4,7,2,1))