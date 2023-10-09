def righttriangle(z):
    nums = [str(i) for i in range(1,z+1)]
    for x in range(1, z+1):
        print(' '.join(nums[0:x]))
    return ''

def isoscelestriangle(x):
    nums = [str(i) for i in range(1, 2*x)]
    for a in range(x):
        num = ''.join(nums[0:((2*a) + 1)])
        numspaces = (x - 1 - a)
        print(' '*numspaces + num)
    return ''

def kite(x):
    nums = [str(i) for i in range(1, 2*x)]
    for a in range(x):
        num = ''.join(nums[0:((2*a) + 1)])
        numspaces = (x - 1 - a)
        print(' '*numspaces + num)
    for b in range(x-1):
        c = (2*b) + 2
        num = ''.join(nums[0:(len(nums) - c)])
        numspaces = int((len(nums) - len(str(num)))/2)
        print(' '*numspaces + num)
    return ''


def halfkite(z):
    nums = [str(i) for i in range(1,z+1)]
    for x in range(1, z+1):
        print(' '.join(nums[0:x]))
    for y in range(1,z):
        print(' '.join(nums[0:(len(nums) - y)]))
    return ''


def X(z):
    nums = [str(i) for i in range(1, 2*z)]
    for a in range(z):
        num = ''.join(nums[0:(len(nums) - 2*a)])
        numspaces = int((len(nums) - len(num))/2)
        print(' '*numspaces + num)
    for b in range(1, z):
        num = ''.join(nums[0:(2*b + 1)])
        numspaces = int((len(nums) - len(str(num)))/2)
        print(' '*numspaces + num)
    return ''

question = ''
while question != 'Exit':
    print("""
    ==========MENU==========
    1. Right-angled triangle
    2. Isosceles triangle
    3. Kite
    4. Half Kite
    5. X
    6. Exit
    ========================
    """)

    question = input('Enter the name of the pattern from the above menu that you want to print: ')

    if question == 'Right-angled triangle':
        n = int(input('Enter the number of lines that you want to print: '))
        print('\n')
        print(righttriangle(n))

    if question == 'Isosceles triangle':
        n = int(input('Enter the number of lines that you want to print: '))
        if n%2 == 0:
            print('\n')
            print(isoscelestriangle(n))
        else:
            print('Enter an even number of lines.')

    if question == 'Kite':
        n = int(input('Enter the number of lines that you want to print (enter an even number of lines): '))
        if n%2 == 0:
            print('\n')
            print(kite(n))
        else:
            print('Enter an even number of lines.')     

    if question == 'Half Kite':
        n = int(input('Enter the number of lines that you want to print: '))
        print('\n')
        print(halfkite(n))

    if question == 'X':
        n = int(input('Enter the number of lines that you want to print: '))
        if n%2 == 0:
            print('\n')
            print(X(n))
        else:
            print('Enter an even number of lines.')

    if question == 'Exit':
        print('\n')
        break
