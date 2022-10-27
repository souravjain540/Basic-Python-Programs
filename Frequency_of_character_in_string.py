sentence = "GeeksforGeeks"
  
frequency = {char : sentence.count(char) for char in set(sentence)}
  
print ("The count of all characters is : "+  str(frequency))