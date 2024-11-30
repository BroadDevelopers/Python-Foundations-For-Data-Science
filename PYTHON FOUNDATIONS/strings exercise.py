"""
create 3 variables to store street,city and country, now create address variable to store entire address.
use two ways of creating this variable, one using + operator and the other using f-striing. print the address
in such a way that street, city and country prints in a seperate line
"""
street_name= "12 gunga street"
city="Bungazu"
country="Kenya"
address1=street_name+'\n '+city+'\n '+country
address2=f'{street_name}\n {city}\n {country}'
print(address1)
print(address2)
"""
create a variable to store the string "Earth revolves around the sun"
i) Print "revolves" using slice operator
ii) print "sun" using negative index
"""
var_string="earth revolves around the sun"
print("printing string revolve:",var_string[5:14])
print("printing the sun using negative index:",var_string[-3:])
"""
create two variable to store how many fruits and vegetables you eat in a day. Now print
"i eat x veggies and y fruits daily" where x and y present vegetables and fruits that you eat everyday
use python f string for this
"""
x=10
y=12
food_string=f'i eat {x} veggies and {y} fruits daily'
print(food_string)
"""
i have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement the correct statement is
'maine 10 samosa khaye'. Replace incorrect words in original string with the new ones and print the new string
also try to do this in one line
"""
t='maine 200 banana khaye'
t=t.replace('200','10')
t=t.replace('banana','samosa')
print("double line replacement:",t)

new_t=t.replace('200','10').replace('banana','samosa')
print('single line replacement:',new_t)