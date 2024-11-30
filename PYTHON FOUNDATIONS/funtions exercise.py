"""
#1write a function called calculate_area that takes base and height as an input and
returns the area of a triangle
equation of an area of a triangle is area=(1/2)*base*height
2.
modify above function to take third parameter shape type. it can be either triangle or rectangle
based on shape type it will calculate are
equation of a rectangles area is
rectangle area=length*width
3.
write a function called print_pattern that takes  integer as an argument and prints following pattern if input number is
3
*
**
**
if input is 4 then it sould print
*
**
***
***
"""
#1
def calculate_area(base,height):
    area=(1/2)*base*height
    return area

tri=calculate_area(5,7)
print(tri)
#2

#3
for i in range(1,6):
    s=""
for j in range(i):
    s+="*"
    print(s)


