x = 0
#int(input("Enter the value of x"))
match x:
    case 0:
      print("value is zero")
    case 1:
        print("Value is one")
     case_: # underscore(_) is used for default
         print(x)