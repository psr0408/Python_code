# enumerate function in python
marks = [23,43,54,65,75,46]
#index = 0
for mark in enumerate(marks):
    print(mark)
#for mark in marks:
   # print(mark)
  #  if (index ==3):
 #       print("Harry marks is 65")
#    index +=1

#for mark,index in enumerate(marks):
#    print(index)
#    if(mark==3):
#        print("harry marks are 65")
#print("\n")
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
     print("harry marks are 65") 
#for v in enumerate(marks): # print tupple hoga
 #   print(v)
   # if(index==3):
    #    print("harry marks are 65")
print("\n")
for index,mark in enumerate(marks,start=1):# start =  1 likne se index 1 se start hoga 0 se ni
    print(mark)
    if(index==3):
     print("harry marks are 54") 
print("\n")  
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
     print("harry marks are 65") 
     