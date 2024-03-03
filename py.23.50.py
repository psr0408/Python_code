#read( )  readlines()
#f = open('myfile11.txt', 'r')
#i = 0
#print(f.read())
#while True:
    #i = i + 1
    #line = f.readline()
    #if not line:
      #  print(line)
     #   print(type(line))
    #    break
    #m1 = line.split(",")[0]
    #m2 = line.split(",")[1]
    #m3 = line.split(",")[2]
    #print(f"The marks of student {i} in maths is:{m1}")
    #print(f"The marks of student {i} in eng is:{m2}")
    #print(f"The marks of student {i} in dc is:{m3}")
    #print(line)
    
   # print(line)
# readline() = read a file by, line by line

f = open('myfile11.txt', 'w')


line = ['line1\n', 'line2\n', 'line3\n']
f.writelines(line)
f.close