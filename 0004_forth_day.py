#bubble sort is an algorithm that sorts an array from the lowest to the highest value.
#1
#bubble sorting non-optimized version
import array as arr

my_array = [5, 2, 9, 1, 5, 6]

n= len(my_array)         #gives the length of the array
for i in range(n-1):       #loop through the array
    for j in range(n-i-1):            #loop through the array
        if my_array[j]> my_array[j+1]:         #if the current element is greater than the next element, swap them
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array is:", my_array)

#2
#bubble sorting which is optimized to stop the algorithm if the inner loop didn't cause any swap.

my_array2 = [3,5,7,9,19,25]

n=len(my_array2)         #gives the length of the array
for i in range(n-1):
    swapped = False 
    for j in range(n-i-1):
        if my_array2[j] > my_array2[j+1]:
            my_array2[j],my_array2[j+1] = my_array2[j+1], my_array2[j]
            swapped = True

    if not swapped:
        break

print("Sorted array:",my_array2)

#3
#selection sort algorithm finds the lowest value in the array and moves it to the front of the arrat.

my_array3 =[64, 25, 12, 22, 11]

n = len(my_array3)
for i in range(n-1):          #loop through the array
    min_index = i               #initialize the index of the minimum element
    for j in range(i+1, n):       #loop through the array starting from the next element
        if my_array3[j] < my_array3[min_index]:       #if the current element is less than the minimum element, update the index of the minimum element
            min_index = j                             #assign the index of the minimum element to the current index
    min_value = my_array3.pop(min_index)          #remove the minimum element from the array
    my_array3.insert(i, min_value)                #insert the minimum element at the beginning of the array

print("Sorted array:", my_array3)

#4
#another example of selection sort array
my_array = [43,56,46,34,7,86]

n=len(my_array)        
for i in range(n-1):
    min_index = i

    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("sorted array",my_array)
