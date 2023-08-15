# Method overriding

class Animal():
    def __init__(self):
        pass

    def print_animal(self):
        print("I am from Animal class.")
    
    def print_animal_two(self):
        print("Iam from Animal class.")

class Lion(Animal):
    
    def print_animal(self):
        print("I am from Lion class")

lion = Lion()
lion.print_animal()
lion.print_animal_two()