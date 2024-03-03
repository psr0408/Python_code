# seek( ) , tell() in python
#with open('myfile11.txt', 'r') as a:
#a = open('myfile11.txt', 'r')
#print(type(a))
    
#a.seek(10) # first 10 index skip kr do ya kr dega
#print(a.tell()) # it tell kha se start ho raha hai ya kitne index skip kr diye hai
#data = a.read(5)
#print(data)

a = open('myfile11.txt', 'w')
a.write('Hello My dear friend')
a.truncate(7)

a = open('myfile11.txt', 'r')
print(a.read())