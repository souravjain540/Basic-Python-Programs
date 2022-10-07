# Contributed by Shrimad-Bhagwat
import math
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))


#a(x)**2+b(x)+c=0
d=(b**2) - (4*a*c)
sqrt_val = math.sqrt(abs(d))
if a!=0:

    if (b*b)<(4*a*c):
        print("Roots are complex.") 
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val) 
    elif (b*b)==(4*a*c):
        print("Real and equal roots.")
        print(-b/(2*a))
        print(-b/(2*a))

    elif (b*b)>(4*a*c):
        print("Real and different roots.")
        
        ans1= (-b+sqrt_val)/(2*a)
        ans2= (-b-sqrt_val)/(2*a)
        print(ans1,ans2)
else:
    print("Not a quadratic equation")