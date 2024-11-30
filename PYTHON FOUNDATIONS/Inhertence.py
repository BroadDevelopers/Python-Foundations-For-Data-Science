"""

Subclasses takng the properties of a
main class
"""

class Vehicle():
    def gen_use(self):
        print("general use: transportation")

class Car(Vehicle):
    def __int__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True

    def spec_usage(self):
        self.gen_use()
        print("Specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __int__(self):
        print("I am a motor cycle")
        self.wheels = 2
        self.has_roof = False

    def spec_usage(self):
        self.gen_use()
        print("Specific use: road trip, racing")

c = Car()
m = MotorCycle()

print(issubclass(Car,Vehicle))
print(isinstance(c,Car))
"""
is instance tells if an object is an instance of a specific callss
 and is subclass method
"""

"""
Benefits of inheritence:
1.Code reuse
2.Extensibility
3.Readability
"""