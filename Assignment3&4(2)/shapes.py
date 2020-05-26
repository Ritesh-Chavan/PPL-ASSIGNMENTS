from abc import ABC, abstractmethod
import turtle, time, math

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

class Shapes(ABC):
   

    @abstractmethod
    def draw(self):
        pass     

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def noside(self, no_side):
        pass


class square(Shapes):

    def __init__(self, side):
        self.side = side
        self.no_side = None
    
    def set_side(self,side):
        self.side = side
        
    def get_side(self):
        return self.side

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4*self.side

    def noside(self, no_side):
        self.no_side = no_side
        print('The square has got', self.no_side,'sides...')

    def draw(self):
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        time.sleep(2)


class rectangle(Shapes):

    def __init__(self, length, breadth):
        self.length = None
        self.breadth = None
        self.no_side = None
    
    def set_side(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def get_side(self):
        return self.length, self.breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def noside(self, no_side):
        self.no_side = no_side
        print('The rectangle has got', self.no_side,'sides...')    
    
    def draw(self):
        t.forward(self.length)
        t.left(90)
        t.forward(self.breadth)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.breadth)
        time.sleep(2)
 
    
class circle(Shapes):
     
    def __init__(self, rad):
        self.rad = None
        self.no_side = None

    def set_rad(self, rad):
        self.rad = rad
        
    def get_rad(self):
        return self.rad

    def area(self):
        return 2 * math.pi * (self.rad ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.rad

    def noside(self):
        self.no_side = 0
        print('The circle has got', self.no_side,'sides...')    
    
    def draw(self):
        t.circle(self.rad)   


class eq_triangle(Shapes):

    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side
        
    def get_side(self):
        return self.side

    def area(self):
        return 0.4 * (self.side ** 2)
    
    def perimeter(self):
        return 3 * self.side

    def noside(self, no_side):
        self.no_side = no_side
        print('The triangle has got', self.no_side,'sides...')    
    
    def draw(self):
        t.forward(self.side) # draw base
        t.left(120)
        t.forward(self.side)
        t.left(120)
        t.forward(self.side)


class rt_triangle(ABC):
    
    def __init__(self):
        self.no_side = None
        self.base = None
        self.height = None
        self.hypo = None
    
    def set_side(self, base, height, hypo):
        self.base = base
        self.height = height
        self.hypo = hypo
        
    def get_side(self):
        return self.base, self.height, self.hypo
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return (self.base + self.height + self.hypo)

    def noside(self, no_side):
        self.no_side = no_side
        print('The triangle has got', self.no_side,'sides...')    
    
    def draw(self): 
        t.forward(self.base) # draw base
        t.left(90)
        t.forward(self.height)
        t.left(135)
        t.forward(self.hypo)
 
class parrallelogram(Shapes):
    
    def __init__(self):
        self.no_side = None
        self.side1 = None
        self.side2 = None
        self.ht = None

    def set_side(self, side1, side2, ht):
        self.side1 = side1
        self.side2 = side2
        self.ht = ht
    
    def get_side(self):
        return self.side1, self.side2, self.ht

    def area(self):
        return self.side1 * self.ht
    
    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def noside(self, no_side):
        self.no_side = no_side
        print('The parallelogram has got', self.no_side,'sides...')    
    
    def draw(self):
        t.forward(self.side1)
        t.right(110)
        t.forward(self.side2)
        t.right(70)
        t.forward(self.side1)
        t.right(110)
        t.forward(self.side2)
        time.sleep(2)


class reg_pentagon(Shapes):
    
    def __init__(self):
        self.side = None
        self.apo = None
        self.per = None
        self.no_side = None
    
    def set_side(self, side, apo):
        self.side = side
        self.apo = apo
    
    def get_side(self):
        return self.side

    def area(self):
        self.per = 5 * self.side
        return 0.5 * self.per * self.apo
    
    def perimeter(self):
        self.per = 5 * self.side
        return self.per

    def noside(self, no_side):
        self.no_side = no_side
        print('The pentagon has got', self.no_side,'sides...')

    def draw(self):
        for i in range(5):
            t.forward(self.side) 
            t.right(72)
        time.sleep(2)
    

class reg_hexagon(Shapes):
    
    def __init__(self, side):
        self.side = side

    def set_side(self,side):
        self.side = side
        
    def get_side(self):
        return self.side

    def area(self):
        return 2.59 * (self.side ** 2)
    
    def perimeter(self):
        return 6 * self.side

    def noside(self, no_side):
        self.no_side = no_side
        print('The hexagon has got', self.no_side,'sides...')

    def draw(self):
         for i in range(6):
            t.forward(self.side) 
            t.right(60)


