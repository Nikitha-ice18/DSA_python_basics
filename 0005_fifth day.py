

#1
#selection sort example
import array

my_array = [34,46,45,56,86,23]

n=len(my_array)

for i in range(n-1):
    min_index=i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)     # we use pop to remove and return the element
    my_array.insert(i, min_value)


print("sorted array is", my_array)


#2
#bubble sort example

my_array = [23,45,13,44,67]

n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

print(my_array)
        
#3

my_array = [21,32,42,55,22,21,11]

n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

print("sorted array is",my_array)

#4

my_array = [23,13,45,24,654,13]

n=len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:

            min_index=j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("sorted array is", my_array)

#5
#insertion sort 


my_array = [7,35,25,57,23,42,11,12,2,4]

n=len(my_array)      #gives the length of the array

for i in range(1,n):     #intializes the positions of values from one to n 
    insert_index = i        
    current_value =  my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] >  current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print('Sorted array', my_array)



