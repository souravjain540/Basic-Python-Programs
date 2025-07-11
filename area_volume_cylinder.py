r=int(input("Enter the radius:"))
h=int(input("Enter the height:"))
def area(r,h):
  return(2*3.14*r*h+2*3.14*r*r)
def vol(r,h):
  return (3.14*r*r*h)
print(f"The Area:{area(r,h):.2f}")
print(f"The Volume:{vol(r,h):.2f}")
