a = int(input("Enter 1 to convert into code\nEnter 0 for to decode\n"))
try:
 if(a==1):
  st = input("Enter message to converted in code\n")
  words = st.split(" ")

  coding = True
  if(coding):
     nwords = []
     for word in words:
      if(len(word)>=3):
        f1  = "gsd"
        f2 = "gsy"  
        st1 = f1 + word[1:] + word[0] + f2        
        nwords.append(st1)
        print(" ".join(nwords))
      else:
           nwords.append(word[ ::-1])
           print(" ".join(nwords))
  else:
   
      nwords = []
      for word in words:
       if(len(word)>=3):
        f1 = "fds"
        f2 = "gsy"
        st1 =  word[3:-3] 
        st1 = st1[-1]      + st1[:-1]
        nwords.append(st1)
       else:
           nwords.append(word[::-1])
           print(" ".join(nwords))
 elif(a==0):

  st = input("Enter message to converted in decode\n")
  words = st.split(" ")

  coding = False
  if(coding):
     nwords = []
     for word in words:
      if(len(word)>=3):
        f1 = "fds"
        f2 = "gsy"  
        st1 = f1 + word[1:] + word[0] + f2        
        nwords.append(st1)
        print(" ".join(nwords))
      else:
           nwords.append(word[ ::-1])
           print(" ".join(nwords))
  else:
   
      nwords = []
      for word in words:
       if(len(word)>=3):
        f1 = "fds"
        f2 = "gsy"
        st1 =  word[3:-3] 
        st1 = st1[-1]      + st1[:-1]
        nwords.append(st1)
       else:
           nwords.append(word[::-1])
           print(" ".join(nwords))
 else:
     print(a,"is not an correct input")

except:
    print(a,"is not an correct input")
    print("Please enter correct input")
    