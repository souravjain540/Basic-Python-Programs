# Write a program that prints the numbers from 1 to 100. For multiples of three, print 
# "Fizz" instead of the number. For multiples of five, print "Buzz" instead of the number. 
# For numbers that are multiples of both three and five, print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# In this code, we iterate over the numbers from 1 to 100 using a for loop. We then use a series of 
# if-elif-else statements to check the divisibility of each number. By checking the divisibility of each number 
# individually and printing the corresponding output, we cover all the necessary cases defined in the FizzBuzz problem.
# The time complexity of this code is O(n), where n is the number of iterations (in this case, 100). The space complexity 
# is O(1) because we are not using any additional data structures that grow with the input size.
# Feel free to run this code, and you'll see the desired FizzBuzz output for the numbers from 1 to 100.