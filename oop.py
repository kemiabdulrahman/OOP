a, b = 50, 78

class Item:
    pay_rate = 4.5
    def __init__(self, name : str ,quantity : int, price: float ):
#        print(f"I am {name}")
        self.n = name
        self.q = quantity
        self.price = price
        assert price >= 0, f"{price} must be greater than or equal to zero"
        assert quantity >= 0, f"{quantity} must be greater than or equal to zero"

    def local_variable(self, initial, final):
        print(final - initial)

    @staticmethod
    def Shop_calculator(quantity, price):
        return quantity * price + 50

    def variables(self, x, y):
        print(self.price * self.q) # class variable
        print(x * y) #local variable
        print(a * b) # Global variable


     # @tech with tim => Add a new attribute 
    def change_quantity(self, quantity):
        self.q = quantity


     # setter, not returning anything 
    def add_year_of_production(self, year):
         self.year = year

        
    def calculate__total_price(self):
        return self.q * self.price * Item.pay_rate


    def apply_discount(self):
       self.price = self.price * self.pay_rate # from the class level i.e Item.pay_rate
       

       # Best practice is to use self instead of Item above i.e from the instance level

Item1 = Item("Phone", 67, 4.00)
Item2 = Item("Biscuit", 23, 8)


Item3 = Item("Egg", 13, 3)
print(Item3.Shop_calculator(Item3.price, Item3.q))
print(Item3.Shop_calculator(90, 90))  # Use of static method

Item4 = Item("Chair", 8, 9)
#print(Item4.variables(100, 300))


# Applying different payrate for this
Item5 = Item("Laptop", 62, 9.54)

# Talking about the apply_discount process. 
Item5.pay_rate = 0.7
Item5.apply_discount()
print(Item5.price)

# Changing Item5 quantity => change_quantity
# Adding a new attribute => add_year_of_production
Item5.change_quantity(6)
print(Item5.q)
Item5.add_year_of_production(2016)
print(Item5.year)


print(Item1.calculate__total_price())
print(Item1.q)
Item1.apply_discount()
print(Item1.price)

# To View all attributes

print(Item.__dict__)
print(Item2.__dict__)
print(Item1.__dict__)






"""
Object reference variable
Object
local variable
Global Variable
Class Variable

"""





"""
Item1 = Item()
Item1.name = "Phone"
Item1.price = 45.00
Item1.quantity = 34
Item1.calculate__total_price(Item1.price, Item1.quantity)


Item2 = Item()
Item2.name = "Laptop"
Item2.price = 67.90
Item2.quantity = 56
Item2.calculate__total_price(Item2.price, Item2.quantity)

"""



"""
# Not related
Item__name = "Biscuit"
Item__price = 23
Item__quantity = 690

print(type(Item__name)) # str
print(type(Item__price)) # int
print(type(Item__quantity))  # int

"""




