from shapes import *

if __name__ == "__main__":
    print('SQUARE:')
    s1 = square(10)
    s1.set_side(100)
    a = s1.area()
    b = s1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    s1.noside(4)
    s1.draw()
    
    t.reset() 
    print('RECTANGLE:')
    r1 = rectangle(10,20)
    r1.set_side(150,100)
    a = r1.area()
    b = r1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    r1.noside(4)
    r1.draw()

    t.reset()
    print('CIRCLE:') 
    c1 = circle(10)
    c1.set_rad(100)
    a = c1.area()
    b = c1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    c1.noside()
    c1.draw()

    t.reset()
    print('EQUILATERAL TRIANGLE:') 
    e1 = eq_triangle(10)
    e1.set_side(150)
    a = e1.area()
    b = e1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    e1.noside(3)
    e1.draw()
    
    t.reset()
    print('RIGHT ANGLED TRIANGLE:') 
    t1 = rt_triangle()
    t1.set_side(65, 72, 97)
    a = t1.area()
    b = t1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    t1.noside(3)
    t1.draw()
    
    t.reset() 
    print('PARRELLELOGRAM:')
    p1 = parrallelogram()
    p1.set_side(200,130, 10)
    a = p1.area()
    b = p1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    p1.noside(4)
    p1.draw()
    
    t.reset()
    print('REGULAR HEXAGON:')
    h1 = reg_hexagon(40)
    h1.set_side(70)
    a = h1.area()
    b = h1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    h1.noside(6)
    h1.draw()
    
    t.reset()
    print('REGULAR PENTAGON:')
    r1 = reg_pentagon()
    r1.set_side(70, 10)
    a = r1.area()
    b = r1.perimeter()
    print('area = {} perimeter = {}'.format(a, b))
    r1.noside(5)
    r1.draw()
