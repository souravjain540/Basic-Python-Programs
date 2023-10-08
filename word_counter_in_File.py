words = 0
file = input("Enter file path : ")        # input file path 
f = open(file, 'r')                       # file opening
line = f.read()                           # file reading
words += len(line.split())                # getting length of list of words
f.close()                                 # closing file
print(words)                              # printing number of words
