# lambda function in python
#def sum(a,b):
    
   #e = a + b
   
   #return e
double = lambda x : x*2
cube = lambda x: x*x*x
sum = lambda a, b: a + b
print(sum(3,4))
print(cube(3))
print(double(5))

def sum1(*a):
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    c = int(input("Enter third number\n"))
    d = a + b + c
    print("The sum of", a, b, "and", c, "is:",d)


print(sum1(0))