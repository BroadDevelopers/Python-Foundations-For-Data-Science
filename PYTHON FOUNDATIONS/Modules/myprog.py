"""
importing modulesself(functions) as a module

import modulesself
area=modulesself.cal_sqr_area(5)
print(area)

"""

"""
you can also import moduluesself as something
samething as the above stateent

import modulesself as f
area1=f.cal_sqr_area(5)
print(area1)
"""


"""
what if myprogr file and modulesself file
are not in the same directory? eg functios file
"""
"""
what you can do us provide a sub directory name
import functions.modulesself as f
area=f.cal_sqr_area(5)
print(area)
"""


"""
what if modulesself is not in a sub directory folder
if we want to this to work well have to use a systems path
youll have to add a path of your c/data science for github directory
by importing a ays module
"""
import sys
sys.path.append("C:\Users\DigitalEthers\Desktop\DATA SCIENCE FOR GITHUB\PYTHON FOUNDATIONS")
import modulesself as f
area=f.cal_sqr_area(5)
print(area)
