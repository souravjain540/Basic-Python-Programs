
#roots of quadratic equation in the form of ax^2 + bx + c = 0
def roots(a,b,c):
    x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    print ("The roots are:", x1, " and ", x2)

a,b,c = input("Enter the values of a, b, and c (seperated by commas) for the equation ax^2 + bx + c = 0 : ").split(',')
roots(float(a),float(b),float(c))
