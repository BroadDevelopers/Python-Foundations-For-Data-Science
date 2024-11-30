"""
let us say your expenses for every month are listed below,
i.january-2200
ii.february-2350
iii.march-2600
iv.april-2130
v.may-2190

create a list to store these monthly expenses and using that find out
1.in feb, how many dollars you spent extra compare to january?
2.find out your total expense in first quarter(first three months) of the year
3.find out if you spent exactly 2000 dollars in any month
4.june month just finished and your expense is 1980 dollar. add this item to our monthly expense list
5.You returned an item that you bought in a month of a april and got a refund of 200 dollar
make a correction to your monthly expense list based on this
"""
exp=[2200,2350,2600,2130]
#1
print("extra dollar spent in feb comp to jan:",exp[1]-exp[0])
#2
total_exp=exp[0]+exp[1]+exp[2]
print("first quarter expenses:",total_exp)
#3
any_month=2000 in exp
print("true or false, 2000 spent in any month:",any_month)
#4
exp.append(1980)
print("expense with june:",exp)
#5
exp[3]=exp[3]-200
print("list with refund:",exp)


"""
heros=["spider-man","thor","hulk","iron man","captain america"]
using this find out
1.lenth of list
2.add "black panther" at the end of the list
3.you realize that you need to add "black panther" after "hulk"
so remove it from the list first and then add it after hulk
4.now you dont like thor and hulk because they get angry easily so you want to remove thor and hulk from the liist
and replace them with doctor strange, do this with one line of code
5.sort the heros list in alphabetical order(hint. used dir() function to list down all functions available in list)
"""
heros=["spider-man","thor","hulk","iron man","captain america"]
#1
print("length for heros list:", len(heros))
#2
heros.append("black panther")
print("heros with plack panther at end of list",heros)
#3
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
#4
heros[1:3]=["doctor strange"]
print(heros)
#5
heros.sort()
print(heros)
