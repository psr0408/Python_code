a = "Harryyy!!!"
print(len(a)) # is for calculate the length of the string
# string are immutable
print(a.upper())# is for print the string in upper case PRASHANT
print(a.lower()) # is for print the string in lower case prashant
print(a.rstrip("!"))# is for strip means ! ki hata dega jo first string or word ke last me hoga
a = "Harry prashant"
print(a.replace("Harry", "John")) # is for replace the name means harry = john
print(a.split(" "))# is for ye string ko shi likta hai just like prashant harry =  'prashant', 'harry'
blogheading = "introduction to HaRry"
print(blogheading.capitalize()) # ye use hota hai captial me likta hai first character ko only first word ka first cahracter
                               # baki sab kuch small me likh dega 

str = "Welcome to home"
print(str.center(200)) # iska mtlb 20 ki space me welcome to home print kar do aur jo space bache wo pahle chod do
print(len(str)) 
print(len(str.center(50)))
print(a.count("Harry")) # string koi cahracter kitni baar aa raha hai isme 1 baar hai isliye ans 1 aayega
str = "Welcome to home!!!"
print(str.endswith("!!")) # ye check krta hai ki last me wo hai toh true ni haii toh false
print(str.endswith("to", 4,10)) # ye check krta hai ki 4 se 9 ki string me last me to hai ki ni hai toh true

print("\n\n")
str = "he is a very good  is"
print(str.find("is")) # ye check krta hai is jo seaarch krna wo kha hai jha par hai uska indeax no milega
print(str.find("igs")) # agr ni hai toh -1 milega
print(str.index("is")) # index is same as find methos lekin agr ni milega toh error aayega
str = "Welcome0tohome"
print(str.isalnum()) # kya string alpha numeric hai ki ni agr hai toh usme A-Z ,a-z, 0-9 ho sakte hai
str = "Welcome to home"
print(str.isalpha())# kya string alpha numeric hai ki ni agr hai toh usme A-Z ,a-z, ho sakte hai
print(str.islower()) # check krega ki all character small hai ki ni
print(str.isupper())# check krega ki all string upper hai ki ni

print("\n\n\n")
print(str.isprintable()) # ye check krta hai ki string print ho sakti hai ki ni jaise agr \n hai toh ye printable ni hai 
str = "  "
print(str.isspace()) # agr spaces hai toh true milega
print("\n")
str = "Welcome to home and Home"
print(str.istitle()) # ye check krta hai ki every word ke starting me captial ki ni 
print(str.startswith("Welco")) # ye check krta haia ki starting me ye hai ki ni 
print(str.swapcase()) # ye lower ko upper case me aur upper case ko lowar me convert krta hai
print("hii")
str = "Welcome to home and Home"

print(str.title()) # every word ka first character captial ho jayega
