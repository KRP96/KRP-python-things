def KRP_max(x,y,z):
    if x>y:
        if x>z:
            print("Maximum number is: ", x)
        else:
            print("Maximum number is: ", z)
    else:
        if y>z:
            print("Maximum number is: ", y)
        else:
            print("Maximum number is: ", z)



def KRP_area_perimeter(x,y):
    print(f"The area of the rectangle is {x} in length and {y} in width is", x*y)
    print(f"The parimeter of the rectangle is {x} in length and {y} in width is", 2*(x + y))

    

