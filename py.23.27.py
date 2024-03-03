
# Kaun Banega Crorepati Exercise
# use list datatype to store the questions and their correct answer
# display the final amount the person is taking home after playing the game
a = input("Enter your name!\n")
print("Hi", a, " This is Computer Mahasay!")
print("Welcome ", a, "in the Kaun Banega Crorepati")
b = int(input("Enter 1 for start the game\n"))
e = 10000
if(b==1):
    print("How many days in a weak")
    c = int(input("1. 2 days   2. 4 days\n3. 6 days   4. 7 days\n"))
    if(c==4):
            print("Congs your answer is correct")
            print("You won the",e , "amount\n")
            print("How many days in month feb 2023 ")    
            d = int(input("1. 25 days   2. 30 days\n3. 28 days   4. 31 days\n")) 
            if(d==3):
                print("Cong your answer is correct")
                print("You have won",e + 15000, "amount")
                print("Who is India's current Prime Minister")
                f = int(input("1. Narendra Modi   2. Atal Bihari Bajpai\n3. Sonia Gandhi    4. Rahul Gandhi\n"))
                if(f==1):
                    print("Cong your answer is correct")
                    print("You have won",  e + 40000,"amount")
                    print("What is the age of SRK SIR")
                    g = int(input("1. 57   2. 54\n3. 50   4. 56\n"))
                    if(g==1):
                        print("Cong your answer in correct")
                        print("You have won", e  + 65000 , "amount")
                    else:
                        print("Your answer is incorrect")
                else:
                    print("Your answer is incorrect")
            else:
                print("Your answer is incorrect")  
                
        
    else:
          print("Your answer is incorrect")
else:
    print("Please enter correct choice")
