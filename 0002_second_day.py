
#1
# Linear Search Function
def linear_search(arr,target): # Linear search function
    size=len(arr)                   # Get the size of the array
    for index in range(0, size):     # Loop through the array
        if(arr[index]==target):      # Check if the current element is equal to the target

            return index              # Return the index if found
    return -1


my_list=[1,2,3,4,5,6,7,8,9]         
target=3

result = linear_search(my_list,target)

print(result)

# checks if the variable is even or odd and increments it accordingly
var = 7   
for i in range(7):    #it gives the range from 0 to 6
    for j in range(2,10,1): #it gives the range from 2 to 9
    
        if var % 2 == 0:     #it checks if the variable is even or not
            continue
        else:
            var += 1
print(var)

#another example of checking if the variable is even or odd and increments it accordingly
#3
num=5
for i in range(7):    #it gives the range from 0 to 6
    for j in range(3,7,1): #it gives the range from 3 to 6
        if num % 2 == 0:     #it checks if the variable is even or not
            continue
        else:
            num += 1         #it increments the variable if it's odd

print(num)


