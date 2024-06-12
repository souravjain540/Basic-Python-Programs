#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

def FizzBuzz(self, n):
    ls=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:ls.append("FizzBuzz")
        elif i%3==0:ls.append("Fizz")
        elif i%5==0:ls.append("Buzz")
        else:ls.append(str(i))
    return ls