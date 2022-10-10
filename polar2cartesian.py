from math import cos, sin

# Read values for r and θ
r = float(input("r = "))
θ = float(input("θ = "))

# Convert polar coordinates to cartesian
x = r*cos(θ)
y = r*sin(θ)

# Print results
print("x = " + str(x))
print("y = " + str(y))
