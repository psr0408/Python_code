# Exception Handling in Python and error handling

a = input("Enter a number:")
print(f"Multiplication table of {a}")
try:
    for i in range(1, 11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as t:
    print("Invalid input")
print("End of program")

#try:
 #   b = int(input("Enter an integer: "))
#except ValueError:
#    print(f"This is not an integer")
#except IndexError:
#    print("Index error")