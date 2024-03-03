# exercise 2 solution to 
import time
time1 = time.strftime('%H:%M:%S')
print(time1)
hour = int(time.strftime('%H'))
print(hour)
if(hour>0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<16):
    print("Good Afternoon Sir!")
elif(hour>=16 and hour<20):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
    