# Contributed by Shrimad-Bhagwat
n=int(input("Enter the no. of rows: "))
for line in range(1, n + 1):  
    c = 1   
    x=n 
    y=line  
    for i in range(1, line + 1): 
        print(c, end = " ")
        c = int(c * (line - i) / i)
    print(" ")  