#a = "harry", "Prashant"
#print(a)
#b = "harry prashant"
#print(b.split(" "))

#print(b.lower())
#print(b.upper())
#print(b)
#print(b.replace("harry", "sushant"))
#print(b)
#print(a.replace("harry", "Sushant")) # if string in one then we change if it is two or more it will not be changed
#item = "hi this is prashant kumar singh"
#print(item.capitalize())
#print(item.rstrip(" h"))
#print(b.rstrip(" t"))

#a = "Welcome to home"
#print(a.center(200))
#print(len(a.center(200)))
#print(a.center(100))
#print(len(a.center(100)))
#print(a.endswith("to", 3,14))
#print(a.find("come")) # milega toh index no 
#print(a.find("dsfasg")) # ni mila toh -1 aayega
#print(a.index("Welcome")) # milega toh index no
#print(a.index("welcome")) # ni mila toh error aayega
#b = int(input("Enter a number you want factorial:\n"))
#def factorial(a):
 #   if(a==0 or a==1):
  #      return 1
   # else:
    #    return(a * factorial(a-1))
#print("The factorial of ",b , "is:",        factorial(b))

a = "this is prashant singh "

print(a.isalnum())
print(a.isupper())
print(a.islower())
print(a.isalpha())