print("Enter the Binary Number: ")
bnum = int(input())

hex = 0
mul = 1
chk = 1
i = 0
hnum = []
while bnum!=0:
    rem = bnum%10
    hex = hex + (rem*mul)
    if chk%4==0:
        if hex<10:
            hex = hex+48
            val = chr(hex)
            hnum.insert(i, val)
        else:
            hex = hex+55
            val = chr(hex)
            hnum.insert(i, val)
        mul = 1
        hex = 0
        chk = 1
        i = i+1
    else:
        mul = mul*2
        chk = chk+1
    bnum = int(bnum/10)

if chk!=1:
    hex = hex+48
    val = chr(hex)
    hnum.insert(i, val)
if chk==1:
    i = i-1

print("\nEquivalent Hexadecimal Value = ", end="")
while i>=0:
    print(end=hnum[i])
    i = i-1
print()
