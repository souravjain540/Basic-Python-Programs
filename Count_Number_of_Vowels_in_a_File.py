######## This program counts and returns the number of vowels in a text file. ########

# Ask the user for the name of the file. The file should be in the same folder and should be a text file.
print("Enter the Name of File: ") 

# Convert the name to string and open the file in read mode
fileName = str(input())
fileHandle = open(fileName, "r")

# Declare a variable to store the number of vowels. Initally it is zero.
count = 0

# create an array of all the vowels (upper and lower case) that can be used to compare and determine if a character is a vowel 
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Read each character and compare it to the characters in the array. If found in the vowels array, then increase count.
for char in fileHandle.read():
  if char in vowels:
    count = count+1
    
# Close the file    
fileHandle.close()

# Print the count to the screen for the user to see.
print("\nThe total number of vowels in the text are:")
print(count)
