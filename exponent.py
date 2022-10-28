def exponent(x,y):
	temp = 0
	c = 1
	i = 1
	while i<=y:
		temp = x
		c = c * temp
		i = i + 1
	return c

base = int(input("Enter the base value:"))
power = int(input("Enter the power value:"))
print("The value of {0} ^ {1} is {2}".format(base,power,exponent(base,power))) 

