# Finally Clause Keyword in python
def fun1():
 try:
    l = [1,2,3,4]
    a = int(input("Enter a number\n"))
    print(l[a])
    return 1
 except:
    print("invalid number")
 finally:
    print("It is always excuted because it is the boss")
    
a = fun1()
print(a)