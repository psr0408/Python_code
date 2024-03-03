# recursion in python
# function ke ander function ko call krne ko recurrence kehta hai
a = int(input("Enter a number you want factorial\n"))
def factorial(n):
    if(n==0 or n ==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(a))
# write a program to print fibonacci sequence
