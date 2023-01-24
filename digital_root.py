"""

A digital root of a number can be gitten by adding each of the individual characters until they reach a 1 digit number

e.g

the digital root of 45893 is

4+5+8+9+3

that will give us 29

and adding up digits if 29

2+9

will give us 11

adding that

1+1

will give us 2

"""

def dig_root(n):

    '''

    I will try to implement this without using type casting  in my code

    '''

    div , res = 10, 0

    while n > 0:

        res+=n%div

        n//=div

    return res if res<10 else dig_root(res)

#print(dig_root(45893))

print(dig_root (int(input())))
