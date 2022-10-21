# taking input for 3 sides of the triangle
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculating semi-perimeter of the triangle  
s = (a + b + c) / 2  

# calculating area of the triangle  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of the triangle is:', area)   

