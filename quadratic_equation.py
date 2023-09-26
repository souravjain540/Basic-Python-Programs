import math
from math import sqrt

def quadratic_eq(a,b,c):
    # ax2 + bx + c = 0  
    # Uncomplete quadratic equations
    if b == 0:
        x1 = sqrt(-c/a)
        if -c / a > 0:
            print(f"x1 and x2 equals to {x1}")
        else:
            print(f"x1 equals to {x1}")        
    elif c == 0:
        x1 = 0
        x2 = -b/a
        print(f"x1 equals to 0 and x2 equals to {x2}")
    elif b == 0 and c == 0:
        print(f"x equals 0")
    
    else: 
    # Standard quadratic equations
        disc = b**2 - (4*a*c)
        print(f"Discriminant is equals to \"{disc}\"")
        if disc < 0:
            print("There is no roots, discriminant less than zero")
        elif disc > 0:
            x1 = (-b + sqrt(disc)) / (2*a)
            x2 = (-b - sqrt(disc)) / (2*a)
            print(f"x1 is equals to {x1}\n"
                f"x2 is equals to {x2}")
        else:
            x1 = -b / a
            print(f"Equation have 1 real root, x is equals to {x1}")
        
a = input("Enter coefficient of a: ")
b = input("Enter coefficient of b: ")
c = input("Enter coefficient of c: ")

try:
    quadratic_eq(int(a),int(b),int(c))
except ValueError:
    print("Your input must be an integer!")