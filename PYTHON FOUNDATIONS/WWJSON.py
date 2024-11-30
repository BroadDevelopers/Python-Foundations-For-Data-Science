"""
JSON=JavaScript Object Notation
JSON is a data exchange format similar to XML
opens and closes with curlybrackets({})
{
 key:value
}
stores data into key value pairs
"""
"""
We will write a program
1. To create an address book and write some records in it
and we will save it as a file on our computer
2.a second program to read the address book and
and print those address book recods
"""
"""
First we will create a dictionary object for this
"""
book={}
book['tom'] = {
    'name': 'tom',
    'address': '1 green street, NY',
    'phone': 999999
}

book['bob'] = {
    'name': 'bob',
    'address': '1 yellow street, NY',
    'phone': 2345678
}

"""
Now we import a JSON module
once imported we call a method called "dumps"
"Dumps" takes the dictionary object(book) which is book
as an input and it is dumping it as a string 
and when it converts it(book-objetc) as a string it will covert it to a JSON format
string "s" will be in JSON format

import json
s=json.dumps(book)
print(s)
"""


"""
Now we will write this to a file
"""
import json
s=json.dumps(book)
with open('C:\\Users\\DigitalEthers\\Desktop\\DATA SCIENCE FOR GITHUB\\PYTHON FOUNDATIONS\\JSON\\book.txt',"w") as f:
    f.write(s)

"""
The advantage now is that you can now open
C++ and JavaScript programme to open book.txt
and read the object thats why its called data exchange
programme
"""