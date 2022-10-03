def linearsearch(lst, x):

    for i in range(len(lst)):
        if lst[i] == x:
            return f'Element {x} found at index {i}'

    return 'Element not found in the list.'

list_in = list(map(int, input("Enter integers seperated by space: ").split()))
x = int(input("Enter X: "))

print(list_in)
print(linearsearch(list_in, x))