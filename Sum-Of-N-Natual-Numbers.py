# Sum of n natural numbers
# for n=4, output = 1+2+3+4 = 10
# for n=9, output = 1+2+...+9

# taking input
n = int(input("Enter n : ")) 

# using mathematical formula n(n+1)/2 
sum = ( n * (n+1) ) / 2
    
# printing output
print(f"Output : {sum}")