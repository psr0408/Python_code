# function arguments in  python
#def gmean(a,b):
 #   gemetricmean = (a*b)/(a+b)
  # gemetricmean = (int(a)*int(b))/(int(a)+int(b))
 #   print("The gemetric mean of ", a, "and", b,"is:",gemetricmean)
     
    
#a = float(input("Enter first number\n"))
#b = float(input("Enter second number\n"))
# gmean(int(a),int(b))
#gmean(a,b)
#def average(a,b): # a, b is required argument here
#def average(a =3, b = 7 ): # this is default argument
 #   print("The average is ", (a+b)/2)
    
#average(4,5) 
#def avg(a, b= 3): # a is required argument
#def avg(a = 3, b = 6):
 #   print("The average is ", (a+b)/2)
    
#avg(b = 12) # hm aise bhi likh skte hai
#avg(a = 12)
#def name(fname, mname = "Singh", lname="Thakur"):
 #   print("Hello,", fname, mname, lname)

#name("Prashant", lname = "Rajawat" )
   
#def average(*numbers): # * means as a tupple value lega
 #   sum = 0
 #   for i in numbers:
 #       sum = sum + i
       #  return sum/len(numbers)
 #   print("Average is ", sum/len(numbers))
        
#average(5,6, 5,61)
def name(**neither): #  ** means jo bhi value  lega as a dicitonary me lega
   # print(type(neither))
  #  print(type(name))
    print("hello,", neither["fname"], neither["mname"], neither["lname"])
    
name(fname = "Prashant", mname = "Singh", lname = "Rajawat")