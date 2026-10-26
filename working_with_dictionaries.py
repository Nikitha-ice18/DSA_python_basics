#All things related to dictionaries in python

#creating a ditionary

my_dict = {
    "name":"John",
    "age":21,
    "city":"washington",
    "occupation":"Civil engineer"
}

#accesing values in a dictionary

#print(my_dict["occupation"])
#print(my_dict.get("name"))

#print(my_dict.keys())  #gets all the keys in the dictionary
#print(my_dict.values())  #gets all the values in the dictionary

### updating values in a dictionary
my_dict.update({"occupation":"software engineer"})

### adding items to a dictionary

my_dict["Date of birth"] = "01/01/2000"

#adding : it adds a new key-value pair to the dictionary if the key does not exist, otherwise it updates the value of the existing key.
#updating : it updates the value of an existing key in the dictionary. If the key does not exist, it adds a new key-value pair to the dictionary.

#removing items in dictionaries

#my_dict.pop("age")  #removes the key-value pair with the specified key from the dictionary
#del my_dict["city"]
#del my_dict
#print(my_dict)  #this will raise an error because the dictionary has been deleted


###Looping through a dictionary

#for x in my_dict:
#    print(x) #prints the keys in the dictionary

#for x in my_dict:
#    print(my_dict[x]) #prints the values in the dictionary

#for x,y in my_dict.items():
#    print(x,y) #prints the key-value pairs in the dictionary

###copying dictionaries

thisdict = my_dict.copy()
#print(thisdict)  #prints the copied dictionary

#creating nested dictionaries

myclassroom ={
    "studen1" : {
        "name":"Nagi",
        "age":18,
        "year":2009
    },
    "student2" : {
        "name":"John",
        "age":19,
        "year":2008
    },
    "student3" : {
        "name":"Mary",
        "age":20,
        "year":2007
    }

}

#print(myclassroom)

#Accessing items in nested dictionaries

#print(myclassroom["studen1"]["name"])  #prints the name of student1

###Looping through nestes dictionaries

for x, obj in myclassroom.items():
    print(x)

    for y in obj:
        print(y +':',obj[y])


#the reason we used obj here is because we are looping through the items in the myclassroom dictionary, and each item is a key-value pair 
# where the key is the student name (e.g., "student1") and the value is another dictionary containing the student's details
#  (e.g., {"name":"Nagi", "age":18, "year":2009}).

