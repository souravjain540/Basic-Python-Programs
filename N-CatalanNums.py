# A Binomial coefficient based function to find nth catalan number in O(N) time

# Catalan numbers are defined as a mathematical sequence that consists of 
# positive integers, which can be used to find the number of possibilities of
# various combinations. 

#The first few Catalan numbers for n = 0, 1, 2, 3, … are : 1, 1, 2, 5, 14, 42, 132, 429,…  


def binomialCoefficient(n, k):
 
    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k
 
    # initialize result
    res = 1
 
    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res
  
 
def catalan(n):
    c = binomialCoefficient(2*n, n)
    return c/(n + 1)
 

#################### Driver Code #####################

# To prompt the user to input an integer we do the following:
valid = False

while not valid: #loop until the user enters a valid int
    try:
        n = int(input('Enter the number of Catalan Numbers you want: '))
        valid = True #if this point is reached, x is a valid int
    except ValueError:
        print('Please only input digits')

for i in range(n):
    print(catalan(i), end=", ")
