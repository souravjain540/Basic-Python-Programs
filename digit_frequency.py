def digit_frequency(n):
    
    n_str = str(abs(n))  
    freq = {}

    
    for digit in n_str:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1

    return freq


number = int(input("Enter an integer: "))
result = digit_frequency(number)


print("Digit frequencies:")
for digit, count in result.items():
    print(f"{digit}: {count}")

