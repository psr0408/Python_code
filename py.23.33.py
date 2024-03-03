# dictionaries in python
dic = {
    "Harry" : "Human Being",
    "Prashant": "Good Human",
    333: "harry"
}
#a = input("Enter a name:")
#if (a=="Prashant"):
 #   print(dic["Prashant"])
#else:
 #   print(a, "is not present")
#print(dic[333])
info = {"name": "prashant", "age": "18"}
#print(info)
#print(info["name"]) # if name is not exist it show error
#print(info.get('name')) # if name is not exist it show none

#print(info.keys()) # name age are keys
print(info.values()) # it print value like prashant and 18
print("\n\n")
print("\n\n")
for key in info.keys():
 print(info[key]) # it print prashant and 18
 print(f"The value corresponding to the {key} is {info[key]}")
print(info.items())
for key, value in info.items():
    print(f"THe value is {key} is {value}")