"""
you have a football field that is 92 meter long and 48.8 meter wide.
find the total area using python and print
"""
field_length=92
field_width=48.8
total_area=field_width*field_length
print('tota; field area:',round(total_area,3))
"""
you bought 9 packets of potato chips from a store, each packet costs
1.49 dollar and you gave shopkeeper 20 dollar. find out ising python 
is the shopkeeper going to give back
"""
packet_chip=1.49
chip_aqu=packet_chip*9
paid=20
change=paid-chip_aqu
print("change will be:", change)
"""
you want to replace tiles in your bathroom which is exactly square and 5.5 feet in length
if tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles
calculate the cost using python (jint:use power ** operator to find area of a square)
"""
bath_len=5.5
bath_area=bath_len**2
rep_cost=bath_area*500
print('cost to replace bathroom tiles:',rep_cost)
"""
print binary representation of number 17
"""
num=17
binary=format(num,'b')
print('binary representation of number 17:',binary)