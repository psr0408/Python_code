# funcion in python
def gmean(a, b):
    gemetricmean = (a*b)/(a+b)
    print("The gemetric mean of ", a, "and", b,"is:",gemetricmean)

#a = int(input("Enter first number"))
#b = int(input("Enter second number"))
#gmean(a,b)
def whoisbig(a, b):
 if(a>b):
    print("The value of ", a," is greather than", b)
 elif(a==b):
    print("Both number are same")
 else:
     print("The value of ", b," is greather than", a)
     
a = int(input("Enter a number:\n"))
b = int(input("Enter second number:\n"))
whoisbig(a, b)
gmean(a,b) 

def less(a,b):
    pass # pass mean baad me likuga abhi error ni aayega pass likne se