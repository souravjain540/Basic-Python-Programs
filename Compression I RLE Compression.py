inp = input("Enter string to compress: ")
counter = 0
curr = inp[0]
output = ""
for i in range(len(inp)):
    if inp[i] == curr:
        counter += 1
    else:
        x = counter // 9
        output += ("9"+curr)*x
        if counter % 9:
            output += str(counter%9) + curr
        curr = inp[i]
        counter = 1

x = counter // 9
output += ("9"+curr)*x
if counter % 9:
    output += str(counter%9) + curr

print(output)