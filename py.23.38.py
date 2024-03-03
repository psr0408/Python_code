# raising custom error in python
a = int(input("Enter a number from 0 to 9\n"))
if(a>=0 and a<=9):
    print("The value you entered is:", a)
else:
    raise ValueError("Value is not between 0 to 9")
    