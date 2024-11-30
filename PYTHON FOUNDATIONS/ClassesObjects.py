"""
Class is an entity formed by methods and class
class is an abstaction of some entity which contains
certain set of properties and methods

class name:
define a function called init- init(self) initializes
the properties of that class when you create an instance
-self means the class itself, and it takes parameters

2nd-define all the
methods
"""

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    def speaks(self):
        print(self.name, "says how are you")

james = Human("james", "actor")
james.do_work()
james.speaks()

serena = Human("serena", "tennis player")
serena.do_work()
serena.speaks()