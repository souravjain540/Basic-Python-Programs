# Python3 program to efficiently compute values
# of euler totient function for multiple inputs.

MAX = 100001;

# Stores prime numbers upto MAX - 1 values
p = [];

# Finds prime numbers upto MAX-1 and
# stores them in vector p
def sieve():

	isPrime = [0] * (MAX + 1);

	for i in range(2, MAX + 1):
		
		# if prime[i] is not marked before
		if (isPrime[i] == 0):
			
			# fill vector for every newly
			# encountered prime
			p.append(i);

			# run this loop till square root of MAX,
			# mark the index i * j as not prime
			j = 2;
			while (i * j <= MAX):
				isPrime[i * j]= 1;
				j += 1;

# function to find totient of n
def phi(n):

	res = n;

	# this loop runs sqrt(n / ln(n)) times
	i = 0;
	while (p[i] * p[i] <= n):
		if (n % p[i]== 0):
			
			# subtract multiples of p[i] from r
			res -= int(res / p[i]);

			# Remove all occurrences of p[i] in n
			while (n % p[i]== 0):
				n = int(n / p[i]);
		i += 1;

	# when n has prime factor greater
	# than sqrt(n)
	if (n > 1):
		res -= int(res / n);

	return res;

# Driver code

# preprocess all prime numbers upto 10 ^ 5
sieve();
print(phi(11));
print(phi(21));
print(phi(31));
print(phi(41));
print(phi(51));
print(phi(61));
print(phi(91));
print(phi(101));


