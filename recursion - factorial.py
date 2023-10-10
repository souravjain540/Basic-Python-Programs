n = int(input("Enter the number:\t"))
def fact(n):
    if n==0:
        return (1)
    else:
        return (n*fact(n-1))
print("Factorial of",n,"=",fact(n))


'''fact(4):
	4*fact(3):
		3*fact(2):
			2*fact(1):
				1*fact(0):
					return 1'''     # TO GET THE OUTPUT WITH BACKTRACKING


# DATA STRUCTURE USED IN RECCURSION IS CALLED STACK AND IT FOLLOWS LIFO TECHNOLOGY i.e LAST IN FIRST OUT
