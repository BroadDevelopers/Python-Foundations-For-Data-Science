""""
1
Create a sample class named Employee
with two attributes id and name
employee :
    id
    name


object initializes id and name dynamically
for every Employee object created.
emp = Employee(1, "coder")

2.
Use del property to first delete id
attribute and then the entire object
"""

class Employee():
    def __int__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f'ID:{self.id} \n Name:{self.name}')

emp = Employee(1,"coder")
emp.display()

# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")