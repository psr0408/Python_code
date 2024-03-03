# tupple in python and it also a data type as list
# tupple cann't be changed
# ( ) this is round bracket
tp = (1,2,3,4, "prashant")
#print(tp)
#print(type(tp))
#print(tp[0])
#print(tp[3])
#print(tp[4])
#print("\n")
#print(tp[-2]) # it means total size - 2 = 5 - 2 = 3 and 3 index value is 4
a = int(input("1. Choose 1 for number\n 2. Choose 2 for string\n"))
if (a==1):
    b =   int(input("Enter the number\n"))
    if b in tp:
        print("This is present")
    else:
        print(b, "This is not present")
else:
    c = input(("Enter the string\n"))
    if c in tp:
        print("This is present")
    else:
        print(c, "This is not present")

#tup = tp[1:3]
#print(tup)
