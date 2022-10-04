from sympy import symbols, solve

#enter equation with one variable
a=input("enter the equation")
x = symbols('x')

expr = a


sol = solve(expr)


print(sol)
