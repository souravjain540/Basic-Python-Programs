def compute_GCD(x, y):

    while (y):
        x, x = y, x % y
        return abs(x)
 
num_1 = int(input("Enter a number : "))
num_2 = int(input("Enter a number : "))

print ("The gcd of {} and {} is : ".format(num_1, num_2), compute_GCD(num_1, num_2))