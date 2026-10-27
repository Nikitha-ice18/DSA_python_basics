
#1
#bubble sort
import array

def bubble_sort(arr):
    n=len(arr) 

    for i in range(n):
        for j in range(n-1):
            if (arr[j]> arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr

unsorted_list=[23,3,43,56,788,654,1]
sorted_list = bubble_sort(unsorted_list)
print("Sorted elements",sorted_list)

#2
#bubble sort

my_array = [9,8,7,6,5,4,3,2,1]

n=len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

print("sorted array is" , my_array)

#3
#selection sort using swaping

my_array = [9,8,7,6,5,4,3,2,1]
n= len(my_array)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if my_array[j] <my_array[min_index]:
            my_array[j],my_array[min_index]=my_array[min_index],my_array[j]

print("sorted array is" ,my_array)


#4 
#insertion sort

def insertion_sort(arr):
    n =len(arr)

    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current-1 #it will go from i-1 to 0

        while correctPosition >=0:

            if (arr[correctPosition]< currentCard):
                break
            else:
                arr[correctPosition +1] = arr[correctPosition]
                correctPosition-=1

            arr[correctPosition +1] = currentCard

    return arr

unsorted_array = [9,8,7,6,5,4,3,2,1]
sorted_array = insertion_sort(unsorted_array)
print("sorted array is",sorted_array)

#practising again and again to master sorting



