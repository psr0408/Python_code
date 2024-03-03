print("Hi")
a =  int(input("Enter your age:"))
print("Your age is :", a)
# conditional operators
# >,< , <=, >=, ==, !=
if(a>=18):
    print("You can drive")
elif(a>=10):
    if(a<=14):
         print("You can drive bicycle")
    elif(a>=15):
          print("You  can driver gear bicycle")
else:
    print("You  cann't drive")
    print("this is only print if else condition is true")
print("yay!")