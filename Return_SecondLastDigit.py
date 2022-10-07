#Python code to extract second last digit of a number using function recursion method

def second_last_digit(n):
    n = n/10;
    if n<=10:
        return -1;
    else:
        return n % 10;

n=int(input("Enter a Number: "))
res = int(second_last_digit(n))  
print("Second Last Digit: ",res)
