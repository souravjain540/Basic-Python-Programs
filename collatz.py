def hailstonenum(n): '''A program for the famous collatz conjecture or hailstone number problem'''
    if(n==1):
        print(n)
        print("\n")
        return 1;
    if(n%2==1):
        print(n)
        print("\n")
        return hailstonenum(3*n+1)
    if(n%2==0):
        print(n)
        print("\n")
        return hailstonenum(n/2)


n = int(input("Enter the number: "))
hailstonenum(n)
