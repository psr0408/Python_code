# set method in python
s1 = {1,2,3,4,5,6}
s2 = {7,8,9,0,3,2}
#print(s1.union(s2))
#print(s1.intersection(s2))
#print(s1,s2)
#s1.update(s2) # insert s2 value in s1
#print(s1,s2)

#s1.intersection_update(s2)
#print(s1,s2)

cities = {"Uttar Pradesh", "Haryana", "Delhi", "Gujrat"}
cities2 = {"Uttar Pradesh","Delhi", "Bilhaur", "Kannuaj", "Mumbai","Haryana", "Delhi", "Gujrat"}
#cities1 = cities2.symmetric_difference(cities) # jo dono me hai wo ni aayega
#cities21 = cities2.difference(cities) #  a - b
#cities.intersection_update(cities2) # jo dono me hai use lega aur update kr dega
#print(cities1)
#print(cities)

#print(cities.isdisjoint(cities2)) #  agar a and b dono alak hai toh true and agar kuch bhi same hai toh false
#print(cities.issuperset(cities2)) # agar cities2 ki  all value cities me hai toh  true 
#print(cities.issubset(cities2)) # cities ki value cities2 me hai toh true
#cities.add("Kaa")
cities.remove("Delhi")
cities.discard("hjkhjkh")
print(cities)
item = cities.pop() # koi bhi ek random value le lega
print(item)
print(cities)
#del cities   # delete the set mtlb jaise set banaya hi ni
cities.clear() # set ke ander ke value ko delete kr dega
print(cities)

if "Delhi" in cities:
    print("Delhi is present")
else:
    print("Delhi is not in the set")
    