# for loop with else statement in python 
#for i in []: # this is an empty list
#for i in range(10):
i = 0
while i<7:
    print(i)
    i = i + 1
    #if i == 4:
     #   break
# else condition tab execute hogi jab loop katam hoga
# agar loop break ho raha hai toh else conditon execute ni hogi
else:
    print("This is not valid")

for y in range(5):
    print("Iteration no {} in for loop".format(y+1))
    if y == 2:
        break
else:
    print("else block in loop ")
print("Out of loop")