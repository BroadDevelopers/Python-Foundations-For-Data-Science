"""
dictionary allowws you to store key value pairs
also known as maps,hashtables, associate arrays
example is a telephone directory{} uses curly brackets
{key:value}
Accessing any element use square brackets and name
d["tom"]-using key
"""
d={"tom":7326789820,"rob":7325730239,"joe":7320923203}
print(d["tom"])
"""
adding a new entry in the dictionary
using square brackets
"""
d["sam"]=7395679879
print(d)
"""
how to delete an entry from a dictionary
use -del- keyword
"""
del d["sam"]
print(d)
"""
how to print all directory values
you can use for loop
key itterates through all the key
"""
for key in d:
   print("key:",key,"value:",d[key])
'''
onother way to do this is to use a tuple
'''
for k,v in d.items():
   print("key:",k,'Value',v)

'''
how to check if a specific name is in a dictionary or not
use in operator
'''
print("tom" in d)
'''
if all phone numbers are changing and we want to trash all the entries

'''
d.clear()
print(d)

'''
Next Topic is Tuplues
tuples- a list of values grouped together
eg representing a geomatric point in a 2D plane
point=(x,y)
'''
point=(5,9)
print(point[0])
print(point[1])
'''
difference between a tuple and a list
List: All values have similar meaning(homogenoues)- eg expense of list of names and expense
tuple: All values have different meaning(heterogenoues)(x,y) eg2 address=("a purple street","new york",10001)
tuples are immutable/cant be changed
'''



