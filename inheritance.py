# Dont confuse database with python class.
# Just Using this examples as an illustration
# Solved specific variables using class variable
# Dunder method, setter and getter method left.
# Use of super()



class Vehicle:
    # Note the Class Variable Created here. Still working for all inherited
    quantity = None
    def __init__(self, price,gas, color):
        self.price = price
        self.color = color
        self.gas = gas

    def fillupTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas 


class Car(Vehicle):
    
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def Beep(self):
        print("Beep Beep")

    def Nitro(self, name):
        print(f"I am a {name} moving with a speed of {self.speed} with a {self.color} color")
    def set_quantity(self, new_Quantity):
        self.quantity = new_Quantity
        
    def display_quantity(self):
        print(f"Quantity Of fuel present == {self.quantity}")



class Truck(Car):
    def __init__(self, price, gas, color, speed, tyre):
        super().__init__(price, gas, color, speed)
        self.tyre = tyre

    def Beep(self):
        print("Beep Beep")


    def __str__(self):
        return f"I am a str(self) moving with a speed of {self.speed} with a {self.color} color"



V1 = Vehicle(100, 123, "white")
C1 = Car(100, 123, "white", "150 Km/hr" )
T1 = Truck(100, 123, "white", "890m/s", 4)


C1.set_quantity("230 litres") 
C1.display_quantity()
print(V1.gas)



T1.fillupTank()
T1.Beep()
T1.set_quantity("500 litres of oil")
T1.display_quantity()

C1.Nitro("Audi")
print(T1.gas)
V1.emptyTank()
T1.Nitro("Caterpillar")
print(V1.gasLeft())

"""
#   Multiple Inheritance    
class Prey:

    def flee(self):
        print("This animal flee")


class Predator:

    def hunt(self, name):
        print(f"This {name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()
hawk.hunt("hawk")
fish.hunt("shark")
fish.flee()
"""
