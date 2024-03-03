import time
# time is a inbuilt module
timea = time.strftime('%H:%M:%S')
 # time.strftime is for time 
print(timea)
hour1 = int(time.strftime('%H'))

if(hour1>=0 and hour1<12):
     print("Good Morning Sir!")
elif(hour1>=12 and hour1<16):
     print("Good Afternoon Sir!")
elif(hour1>=16 and hour1<20):
     print("Good Evening Sir!")
elif(hour1>=20 and hour1<23):
     print("Good night sir")
else:
     print("So Jao Sir Kyuki time bahut ho gya hai like", timea)
     