no_of_rows = int(input("Enter a number : "))
 
for number in range(no_of_rows):
    print(' ' * (no_of_rows - number), end = ' ')
    print(' '.join(map(str, str(11 ** number))))