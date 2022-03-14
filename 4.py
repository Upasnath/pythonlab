x=int(input("enter the length of the square of 1 side\t"))
area=lambda x:x*x
print("area of square is {0}".format(area(x)))

l=int(input("enter the length of the rectangle\t"))
b=int(input("enter the breadth of the rectangle\t"))
area=lambda l,b:l*b
print("area of rectangle is {0}".format(area(l,b)))

b=int(input("enter the breath of the triangle\t"))
h=int(input("enter the height of the triangle\t"))
area=lambda b,h:0.5*b*h
print("area of the triangle is {0}".format(area(b,h)))