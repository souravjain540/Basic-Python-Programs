from math import acos, sqrt, pi

# Read values for x and y
x = float(input("x = "))
y = float(input("y = "))

# Convert polar coordinates to cartesian
r = sqrt(x**2 + y**2)
θ = acos(x/r)
θ *= 1 if y >= 0 else -1

# Print results
print("r = " + str(r))
print("θ = " + str(θ))
