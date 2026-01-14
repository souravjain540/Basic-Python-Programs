"""
Sieve of Eratosthenes - Efficient algorithm to find all primes up to n
Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using Sieve of Eratosthenes
    
    Args:
        n: Upper limit (inclusive)
    
    Returns:
        List of all prime numbers up to n
    """
    if n < 2:
        return []
    
    # Create a boolean array "prime[0..n]" and initialize all entries as true
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it's a prime
        if prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [i for i in range(n + 1) if prime[i]]
    return primes


def segmented_sieve(n):
    """
    Memory-efficient segmented sieve for very large n
    
    Args:
        n: Upper limit
    
    Returns:
        List of prime numbers
    """
    if n < 2:
        return []
    
    # Find all primes up to sqrt(n)
    limit = int(n ** 0.5) + 1
    base_primes = sieve_of_eratosthenes(limit)
    
    # For small n, just return the result
    if n <= limit:
        return [p for p in base_primes if p <= n]
    
    # Use segmented approach for larger numbers
    primes = base_primes.copy()
    segment_size = limit
    
    for low in range(limit + 1, n + 1, segment_size):
        high = min(low + segment_size - 1, n)
        
        # Create a segment
        segment = [True] * (high - low + 1)
        
        # Use base primes to mark multiples in this segment
        for prime in base_primes:
            # Find the minimum number in [low, high] that is a multiple of prime
            start = max(prime * prime, ((low + prime - 1) // prime) * prime)
            
            for j in range(start, high + 1, prime):
                segment[j - low] = False
        
        # Add primes from this segment
        for i in range(len(segment)):
            if segment[i]:
                primes.append(low + i)
    
    return primes


def count_primes(n):
    """
    Count number of primes up to n
    
    Args:
        n: Upper limit
    
    Returns:
        Count of primes
    """
    return len(sieve_of_eratosthenes(n))


if __name__ == "__main__":
    print("=" * 50)
    print("SIEVE OF ERATOSTHENES")
    print("=" * 50)
    
    # Example 1: Find primes up to 30
    n1 = 30
    primes1 = sieve_of_eratosthenes(n1)
    print(f"\nPrime numbers up to {n1}:")
    print(primes1)
    print(f"Count: {len(primes1)}")
    
    # Example 2: Find primes up to 100
    n2 = 100
    primes2 = sieve_of_eratosthenes(n2)
    print(f"\nPrime numbers up to {n2}:")
    print(primes2)
    print(f"Count: {len(primes2)}")
    
    # User input
    print("\n" + "=" * 50)
    try:
        n = int(input("\nEnter a number to find all primes up to it: "))
        
        if n < 2:
            print("No prime numbers exist below 2.")
        else:
            primes = sieve_of_eratosthenes(n)
            print(f"\nPrime numbers up to {n}:")
            
            # Print in rows of 10 for better readability
            for i in range(0, len(primes), 10):
                print(primes[i:i+10])
            
            print(f"\nTotal count: {len(primes)}")
            
            # Show efficiency comparison
            if n >= 1000:
                print(f"\nNote: Found {len(primes)} primes efficiently!")
                print("Sieve of Eratosthenes is much faster than checking each number individually.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
