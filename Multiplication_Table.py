def multiplicationTable(n, i=1):
    if i == 11:
        return
    print(n, 'x', i, '=', n*i)
    multiplicationTable(n, i+1)

n = int(input("Enter the number:"))
multiplicationTable(n)
