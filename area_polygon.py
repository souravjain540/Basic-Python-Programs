n=float(input("Enter no of sides in polygon:"))
r = float(input("Enter the radius of an inscribed circle: "))
l=float(input("Length of one side of the polygon:"))
def area(r):
    return ((n/2)*l*r)
print(f"Area: {area(r):.2f}")
