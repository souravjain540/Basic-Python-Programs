def SieveOfEratosthenes(n):
    numbers = {i: True for i in range(2, n+1)}
    primes = []
    
    p = 2
    
    while p**2 < n :
        if numbers[p] :
            for i in range(p**2, n+1, p):
                numbers[i] = False
        p+=1
    for i in range(2, n+1) :
        if numbers[i] :
            primes.append(i)
    
    return primes
    
def main() :
	n = int(input("Enter value of n to find primes between 1 and n (inclusive):"))
	arr = SieveOfEratosthenes(n)
	print("Primes:", *arr)
	
main()
