"""
after flipping a coin 10 times you get these results
result=["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
2.using a for loop figure out how many times you got heads
3Your monthly expenses list(from january to may) looks like this
expense_list=[2340,2500,2100,3100,2980]
write a program that asks you to enter an expense amount and program should tell you in which month that expense occured
if expense is not found then it should write that as well
"""
#1
result=["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
h=0
for r in result:
    if r=="heads":
        h=h+1
print("heads count",h)
#2
expense_list=[2340,2500,2100,3100,2980]
months_list=["january","february","march","april","may"]
e=input("Enter Expense")
e=int(e)

month=-1
for i in range(len(expense_list)):
    if e==expense_list[i]:
        month=i
        break

if month !=-1:
    print(f'you spent {e} in {months_list[month]}')
else:
    print(f'you didn\'t spend{e} in any month')
"""
lets say you are running a 5km race write a program that
iupon completing 1 km asks you "are you tired"
ii. if you reply yes then it shoukd break and reply "you didnt finish the race"
iii.if you reply no then it should continue and ask "are you tired" on every km
iv.if you finish all 5 km then it should print congradulations message
5. write a program that prints the shape
*
**
***
****
*****
"""
for i in range(5):
    print(f'you ran {i+1} miles')#i starts at zero
    tired=input("are you tired?")
    if tired=='yes':
        break

if i==4: #4 because index starts from zeero
    print("hurray! you finished the 5kn race")
else:
    print("you didnt finish the race", "but you ran {i+1}miles")

#5
for i in range(1,6):
    s=''
    for j in range(i):
        s=s+'*'
    print(s)

