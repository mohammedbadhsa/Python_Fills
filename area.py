import math


def my_area(a,b,c): # ---. Create my own module in python;
    d = b*b-4*a*c
    if(d>0):
        x1 =-b+math.sqrt(d)/(2*a)
        x2 =-b-math.sqrt(d)/(2*a)
        print(f"The roots is :{x1}\nThe Roots is :{x2}")

    elif(d==0):
        x = -b/(2*a)
        print(f"The Roots is {x}")

    else:
        print("The Roots are imeginary")

#my_area(10,60,11)
