"""
 A program that prints the numbers from 1 to N. 
 But for multiples of three print "Fizz" instead of the number 
 and for the multiples of five print "Buzz". 
 For numbers which are multiples of both three and five print "FizzBuzz"
"""

n=20

for i in range(1,n+1):
    output=""
    if i%3 == 0: output+="Fizz"
    if i%5 == 0: output+="Buzz"
    if output: print(output)
    else: print(i)