inp = [
        # [45,35,16,30,36],
        # [32,32,40,31,43],
        # [ 5,11,34,25, 1],
        # [ 7, 2, 8,25,39],
        # [26,18,19, 5,32],
        # [ 5,31, 1,29,40],
        # [ 1,29,14,31,46],
        # [41,47,12,45,34],
        # [35, 2,25, 1,26],
        # [13,11, 4,36,14],
        # [49,26,16,46,42],
        # [46,15, 3,46,29],
        # [ 6,17,18,41,20],
        # [39,38,14,29,41],
        # [ 1, 1,50,13, 8]
    ]
if not inp:
    print("Open the file, and paste the matrix(or uncomment to use the example)")
    exit()

output = []
layer = 0
def right():
    global inp, layer, output
    for i in range(layer, len(inp[0]) - layer):
        if len(output) < len(inp)*len(inp[0]):
            output.append(inp[layer][i])

def down():
    global inp, layer, output
    for i in range(1+layer, len(inp) - layer):
        if len(output) < len(inp)*len(inp[0]):
            output.append(inp[i][-1-layer])

def left():
    global inp, layer, output
    for i in range(len(inp[0])-2-layer, layer-1, -1):
        if len(output) < len(inp)*len(inp[0]):
            output.append(inp[-1-layer][i])

def up():
    global inp, layer, output
    for i in range(len(inp)-2-layer, layer, -1):
        if len(output) < len(inp)*len(inp[0]):
            output.append(inp[i][layer])
    layer += 1

while len(output) < len(inp)*len(inp[0]):
    right()
    down()
    left()
    up()

print(output)