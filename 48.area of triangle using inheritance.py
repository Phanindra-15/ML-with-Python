class Triangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        
        print('The area of the triangle is ' %area)
