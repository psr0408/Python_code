# doc string in python
def square(n):
    '''Takes in a number n, returns the square of n''' # ye comment ni hai ye dog string hai
    print(n**3)
    #print(n)
square(5)
print(square.__doc__) # doc string print hogi isse 
print(type(square.__doc__))