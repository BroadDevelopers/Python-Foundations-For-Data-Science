"""
1create inheritance using animal Dog relation.
for example,
    Animal and Dog both has same habitat so create a method for habitat
2.use super() constructor for calling parent constructor.
class Animal:
    #code
class Dog(Animal):
    super()-it refers Animal class,now you can call Animal's methods.
"""
class Animal:
    def __int__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __int__(self):
        super().__int__("kannel")

    def sound(self):
        print("woof woof")
        
d = Dog()
d.print_habitat()
d.sound()