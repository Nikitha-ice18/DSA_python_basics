#1
#Linear search algorithm
import array as arr

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_array = arr.array('i',[1,2,3,4,5,6,7,8,9])
target_value = 5
print(linear_search(my_array,target_value))

#2
#another example of linear search algorithm

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1
my_array2 = arr.array('i',[4,7,2,9,1])
target_value=9
print(linear_search(my_array2,target_value))

#3
#Linear search algorithm for string array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_array3 = ['nikki','python','java','c++']
target_value = 'python'
print(linear_search(my_array3, target_value))


#4
#gives the first 10 fibonacci numbers using iterative method.
prev2=0
prev1=1

print(prev2)
print(prev1)
for fibo in range(8):
    newFibo = prev1+prev2
    print(newFibo)
    prev2=prev1
    prev1=newFibo

print(0)
print(1)
count =2

#4
#gives the first 20 fibonacci numbers using recursive method.
def fibonacci(prev1, prev2):
    global count
    if count <= 20:
        newFibo = prev1+ prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)

    else:
        return

fibonacci(1,0)

#5
#gives the nth fibonacci number using recursive method.
def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)
print(F(19))

#All the above examples are of linear search algorithm and fibonacci series using iterative and recursive methods.