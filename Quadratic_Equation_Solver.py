from math import sqrt

def solve(a: float, b: float, c: float):
    # Check if there are real roots
    D = (b^2)-(4*a*c)
    
    if (D<0):
        return "Real Roots Don't Exist"
    else:
        r1 = (-b + sqrt(D))/2*a
        r2 = (-b - sqrt(D))/2*a

        return f"The real roots are {r1} and {r2}"

if __name__ == '__main__':
    a: int = int(input("What is the co-efficient of x^2: "))
    b: int = int(input("What is the co-efficient of x: "))
    c: int = int(input("What is the constant value: "))

    print(solve(a,b,c))