"""
string are used to store text data in python
"""
text="ice cream"
print(text)
"""
python stores string in different memory address
ice cream
012345679
individual characters can be accessed using indexes
"""
print(text[0])
print(text[1])
"""
individual characters of a string cant be changed
text[0]='g' will five you an error
accessing substring 'ice' and 'cream'
"""
print(text[0:3])
print(text[4:9])
"""
you can ommit the start and last index
"""
print(text[4:])
print(text[:3])
"""
you can use single and double quotes to store text data
"""
"""
multiline string use tripple quotes
"""
myaddress=""" 1 tokyo street
cape town
ZA
"""
print(myaddress)
"""
you can also use \n to represent new line
"""
address="4 gunga sreet \n polokwane\n south africa"
print(address)
"""
You can use plus sign to concatinate two strings
"""
s1="hello"
s2="world"
word=s1 +' '+s1
print(word)

"""
joining string and integer using str function
"""
s3="total states in usa"
num1=35
print(s3+str(num1))