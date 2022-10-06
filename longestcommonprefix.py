def longestCommonPrefix(a):
      
    size = len(a)
  
    # if size is 0, return empty string 
    if (size == 0):
        return ""
  
    if (size == 1):
        return a[0]
  
    # sort the given strings
    a.sort()
      
    # find the minimum length string
    end = min(len(a[0]), len(a[size - 1]))
  
    # find the common prefix 
    i = 0
    while (i < end and a[0][i] == a[size - 1][i]):
        i += 1
  
    ans = a[0][0: i]
    return ans
  
inputs = []

n = int(input("Enter the number of strings : "))

for i in range(n):
  inputs.append(input("Enter the string : "))

print("The longest Common Prefix is :" , longestCommonPrefix(inputs))