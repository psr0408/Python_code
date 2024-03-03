# map_filter reduce in python
#def cube(a):
  #  d = a * a * a
 #   return d
    
#print(cube(21))

l = [1,2,3,4,5,6]
'''
newl = []
for item in l:
   newl.append(cube(item))
'''  

newl = list(map(cube,l))
print(newl)
def filter_function():
    return a>4
newnewl = filter(filter_function)
a = 0