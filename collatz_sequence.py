# The Collatz Conjecture is a famous math problem. 
# The conjecture is that after applying a sequence of one of two transformations, 
# every positive integer will eventually transform into 1.
# The transformations are: divide by 2 if the number is even, multiply by 3 and add 1 if its odd.
# You can see more about it here https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(initial_number):
    num = initial_number
    print(f'Initial number is: {initial_number}')
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)
        print('Finally!')