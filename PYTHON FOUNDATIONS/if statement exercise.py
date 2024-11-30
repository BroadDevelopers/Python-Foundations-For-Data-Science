"""
#1 using the following list of cities per country,
india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulan","rangpur"]

i.write a program that asks a user to enter a city name and it should tell which country the city belongs to
ii.write a program that asks a user to enter two cities and it tells you if they both are in the same country or not
mumbai and chennai, it will print "both cities are in india" but if i enter mumbai and dhaka it should print "they do not belong to the same country"

"""
india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulan","rangpur"]
#i
city=input("enter a city:")
if city in india:
    print("india")
elif city in pakistan:
    print("pakistan")
elif city in bangladesh:
    print("bangladesh")
else:
    print("None of the countries have a city named:",city)
#2
city1=input("Enter first city:")
city2=input("Enter second city")
if city1 in india and city2 in india:
    print("both cities belong to the same country india")
elif city1 in pakistan and city2 in pakistan:
    print("both cities belong to the same country pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("both cities are from the same country bangladesh")
else:
    print("These cities are not from the same country")
"""
write a program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100
i.ask user to enter his fasting range
ii.if it is below 80 to 100 range then print that sugar is low
if it is above 100 then print that it is high otherwise print that it is normal
"""
#1
slevel=input("input fasting range:")
slevel=int(slevel)
#ii
if slevel<80:
    print("your sugar level is low")
elif  slevel>100:
    print("your sugar level is high")
else:
    print("your sugar level is normal")