#problem 1: sum of digits of a number

def sum_of_digits(n):
    sum=0
    while n>0:
        digit=n % 10
        sum+=digit
        n= n//10
    return sum

n=int(input("Enter a number: "))
result=sum_of_digits(n)
print("Sum of digits:", result)


#problem 2: check if a number is prime

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n=int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")


#problem 3: find the factorial of a number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Enter a number: "))
result=factorial(n)
print("Factorial of", n, "is", result)
