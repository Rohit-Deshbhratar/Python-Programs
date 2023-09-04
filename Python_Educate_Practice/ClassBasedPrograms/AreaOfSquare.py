class Square:

    # Write init and printArea method here.
    def __init__(self, l=10):
        self.length = l
    
    def printArea(self):
        l = self.length * self.length
        print(l)

s1 = Square()
s2 = Square(7)
s1.printArea()
s2.printArea()
