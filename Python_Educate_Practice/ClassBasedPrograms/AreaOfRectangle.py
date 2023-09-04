class Rectangle:    
    length, breadth = map(int, input().split())
    
    def getArea(self):        
       area = self.length * self.breadth        
       print( area )

rect = Rectangle()  
rect.getArea()