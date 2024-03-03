# list in python
# [] square bracket is created a list
l = [3,24,4,3,4,5,6,7] # length is 3 and index is 2
print(l[1:3])
#print(l)
#print((l[0]))
#print((l[1]))
#print((l[2]))
#print("\n")
# tupple  cann't be change 
# list can  be change
# list ke ander aur bhi data type aa sakte hai
# marks = [2,3,4, "Harry", yes ]
print((l[-1]))
print((l[-2]))
print((l[-3]))
print("\n")
print(l[len(l)-1]) # this and 14 is same code

if 5 in l:
    print("yes")
else:
     print("no")
     
print(l)
print(l[:1])
l1 = [2,3,4,5,54,8,86,65,4]
print(l1[1:8:3]) # jump indexing 

print("\n")
l2 = [i*i*i for i in range(10) ]
print(l2)
l2 = [i*i*i for i in range(10) if i%3==0]
print(l2)

marks = [1,2,4,5,6,7,8]
print(marks[0:6:2])