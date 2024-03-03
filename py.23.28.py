# f string in python f-string use for string formatting
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Prashant"
#print(letter.format(name, country))

# use fo f string
#print(f"Hey my name is {name} and  I am from {country}")
price = 49.333
#txt = "For only {price: .2f} dollars!"
txt = "For only {pricea: .2f} dollars!"
print(txt.format(pricea = 33.5343))
print(f"For only {price: .2f} dollars!")
#print(txt)
print(f"{2 * 30}") 
print(type(f"{2 * 30}"))
print(f"Hey my name is {name} and  I am from {{country}}")
print(f"Hey my name is {{name}}'''{{ye bracket do baar lagase se ye aise hi print hoga'''}}and  I am from {country}")
