# Adding new object properties
class Hotel:
    def __init__(self) -> None:
        self.tea = "Tea/ Green Tea/ Black Tea"
        self.coffee = "Black Coffee/ Capachino/ Cold Coffee"
        self.cake = "Cup Cake"
        self.bread = "Pizza/ Paratha"
    
    def items(self):
        print("Menu card...")
        print(f"{self.tea}\n{self.coffee}\n{self.bread}\n{self.cake}")

menu = Hotel()
menu.breakfast = "Wada pav/ Poha/ Upama/ Shira"
menu.items()
print(menu.breakfast)
#####################################################################

# Deleting object properties
class Hotel:
    def __init__(self) -> None:
        self.tea = "Tea/ Green Tea/ Black Tea"
        self.coffee = "Black Coffee/ Capachino/ Cold Coffee"
        self.cake = "Cup Cake"
        self.bread = "Pizza/ Paratha"
    
    def items(self):
        print("Menu card...")
        print(f"{self.tea}\n{self.coffee}\n{self.bread}\n{self.cake}")

menu = Hotel()
menu.items()
del menu.cake
# After deleting "menu.cake"
# menu.items() 
#####################################################################
# Delete object
class Hotel:
    def __init__(self) -> None:
        self.tea = "Tea/ Green Tea/ Black Tea"
        self.coffee = "Black Coffee/ Capachino/ Cold Coffee"
        self.cake = "Cup Cake"
        self.bread = "Pizza/ Paratha"
    
    def items(self):
        print("Menu card...")
        print(f"{self.tea}\n{self.coffee}\n{self.bread}\n{self.cake}")

menu = Hotel()
menu.items()
del menu
# After deleting "menu" object
print(menu)