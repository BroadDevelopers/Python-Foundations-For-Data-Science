"""
using for loop in python
"""
"""
problem: Store monthly expenses in a list and find out 
total expenses for all months
"""
exp=[2340,2500,2100,3100,2980]
#old way total=exp[0]+exp[2]....
total=0
for item in exp:
    total= total + item
print(total)

"""
print numbers rangi from 1 to 10
using range funvtio
range()
range(start,end+1) eg- range from 1 to 10 (1,11)
"""
for i in range(1,11):
    print(i)

"""
in our monthly expense example print the month number and 
espenses and then in the end print total expense
"""
exp=[2340,2500,2100,3100,2980]
total2=0
for ixp in range(len(exp)):
    print("month number:",ixp+1,"expense:",exp[ixp])#ixp+1 beacause ixp starts at index 0, so first expense will be 1
    total2=total2+exp[ixp]
print("expense total:",total)

"""
search for lost key in home and when found stop searchin using break statemnt
"""
key_location="chair"
locations=["garage","living room","chair","closet"]
for loc in locations:
    if loc==key_location:
        print("Key is found in",loc)
        break
    else:
        print("Key was not found in:",loc)

"""
print the square of numbers 1 to 5 except even numbers
using the continue keyword
"""
for s in range(1,6):
    if s%2==0:
        continue
    print(s*s)

"""
print nimbers 1 to five using while loop
while loop only takes one condition
"""
w=1
while w<=5:
    print(w)
    w=w+1