"""
example making a list of items to buy at grocery store
"""
#old version using variables
item1="bread"
item1="pasta"
item1="fruits"
#new version uing list in square brackets[]
items=["braed","pasta","fruits","veggies"]
print(items)
#items are stored in squaence of memory locations
#these locations are accessed by index
print(items[0])
print(items[2])
#list can be modified by index, buying chips intead of bread
items[0]="chips"
print(items)
#accessing a range of elements using sub-index-range
print(items[0:2])
#printing last elemnt in lit
print(items[-1:])
#append adds item at end of list
items.append("butter")
print(items)
#insert(location,string name) items at after bread
items=["braed","pasta","fruits","veggies"]
print(items)
items.insert(1,"butter")
print(items)
#Joining 2 lists using + operator
food=["bread","pasta","fruits"]
bathroom=["shampoo","soap"]
items=food+bathroom
print(items)
#you cant add a string or number using + operator to a list
#print(food+"soda")

#finding length of list using len function
print(len(items))
#wanting to know if you added fruit to the list using in operator
print("bread" in items)
print("soda" in items)