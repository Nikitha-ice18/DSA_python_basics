#1
#Insertion sort
import array

my_array = [32,35,11,14,12,54,3456]

n=len(my_array)
for i in range(1,n):
    insert_index=i
    current_value = my_array.pop(i)
    for j in range(i-1,-1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print("Sorted array:", my_array)

#2
import array
my_array = [45,334,32,53,23,22,13,4]
n = len(my_array)
for i in range(1, n):
    insert_index=i
    current_value = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break

        my_array[insert_index] = current_value

print("sorted array:", my_array)







