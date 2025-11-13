#A Function That Takes A Number 'n' And Then Returns A Randomly Generated Number Having 'n' Digits
#importing Random Module 
import random

def gennum(n):
    lbound=10**(n-1) #lower bound
    ubound=(10**n)-1 #upper bound
    return random.randint(lbound,ubound)

#Taking Input From User
n=int(input("Enter A Number:"))
rnum=gennum(n)
print("Random Number:", rnum)