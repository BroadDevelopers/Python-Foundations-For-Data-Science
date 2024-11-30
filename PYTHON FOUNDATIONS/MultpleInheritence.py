"""
Inhering a class from two different classes
"""

class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")

c = Child()
c.gardening()
c.cooking()
c.sports()

"""
another way
"""
class Father():
    def skills(self):
        print("programming,gardening")

class Mother():
    def skills(self):
        print("art,cooking")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()
