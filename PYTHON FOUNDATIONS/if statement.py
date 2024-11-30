"""
if stament is one of the conditional statement to choose alternatives bertween statement
"""
"""
write a program that asks a user to enter a number
program should then tell if number is odd or even
"""
num=input("enter number")
num=int(num)
if num%2==0:
    print("number is even:")
else:
    print("number is odd")

"""
operator
==-equal to operator
!=-not equal to operator
>-greater than
<-less than
>=greater equal
<=less than equal
and - and operator
or - operator
not true - this mean its false
"""


"""
 write a program that asks user to enter dish name and it
 should print which cuisine is that dish
"""
indian=["samosa","daal","naan"]
chinese=["egg roll","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("enter dish:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Based on our knowledge we dont have dish:",dish)