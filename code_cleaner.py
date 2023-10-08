
def spaceRemover(line):
    return " ".join([i for i in line.split() if len(i) != 0])

def newLinerRemove(line):
    return " ".join([i for i in line.split('\n') if len(i) != 0])


if __name__ == '__main__':
    filePath = input("Enter program file (in c) path : ")
    fileToWrite = open('output.txt', 'w')
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            newline = spaceRemover(line)
            newline = newLinerRemove(newline)
            if len(newline) == 0:
                continue
            fileToWrite.write(newline + "\n")
            
    fileToWrite.close()
