# local and global variable
a = 8
print(f"The global1 variable is {a}")

def Hello():
   global a 
   a = 7
   print(f"The local variable is {a}")
   print("Harry")
    
print(f"The global2 variable is {a}")
Hello()
print(f"The global3 variable is {a}")
