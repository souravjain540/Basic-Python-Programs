# Write a program that prints the numbers from 1 to n. For multiples of three 
# print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzbuzz(n):
  for num in range(1, n+1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 3 == 0:
      print('Fizz')
    elif num % 5 == 0:
      print('Buzz')
    else:
      print(num)

def main():
    # Get n
    user_number = int(input("Enter a number: "))

    fizzbuzz(user_number)

if __name__ == '__main__':
    main()