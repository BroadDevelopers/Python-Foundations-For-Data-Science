"""
functions are a block of code that performs
a specific task
"""
"""
you are given twoo lists of numbers and you
need to find total of each of these lists
def functionName(imput/parametter)
"""
tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

#using aa for loop will cause you to repeat a code over and over for two people
#function simplifies it
def calculate_total(exp):#function
    total=0
    for item in exp:
        total=total+item
    return total#return value

toms_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)
print("tomos total:",toms_total)
print("joes total:",joe_total)

"""
sum of two numbers
"""
total=0
def sum(a,b):
    print("a:",a)
    print("b:",b)

    total=a+b
    print("total inside function:",total)
    return total

n=sum(b=5,a=6)
print("print total outside function:",total)