#Create a Python project that prints out every line of the song "99 bottles of beer on the wall."


for i in range(100, 0, -1):
    if i == 1:
        print(f'''{i} bottle of beer on the wall,
        {i} bottle of beer!
        Take it down,
        Pass it around,
        No more bottles of beer on the wall!\n''')
    else:
        print(f'''{i} bottles of beer on the wall,
        {i} bottles of beer!
        Take one down,
        Pass it around,
        {(i - 1)} bottles of beer on the wall!\n''')
