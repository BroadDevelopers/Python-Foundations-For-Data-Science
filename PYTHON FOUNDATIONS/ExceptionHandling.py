"""
Exceptions are errors that occur while executing
your programme or
exceptions are errors at the time of program execution
"""
"""
we are writing a programme that shows how we handle
exceptions handling
if we cant divide a number by zero were initializing z
as none

try:
    z=int(x)/int(y)
except Exception as e:
    print('exception occured',e)
    z=None
    
    sepcific way of handiling an exception
    
    x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z=None
print("Division is:", z)
"""


"""
Handling multiple exception
when taking number from a console you forget to convert
it to an interger

x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z=None
except TypeError as e:
    print('Exception type:', type(e).__name__)
    z = None
print("Division is:", z) this is a TypeError
"""
x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z=None
except TypeError as e:
    print('Type error exception')
    z = None
print("Division is:", z)