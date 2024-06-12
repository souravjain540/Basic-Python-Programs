sentence ='a sentence cannot start with because because because is a conjunction'
frequency = {}
words = sentence.split()

for word in words:
    if word[-1] == '.':
        word = word[0:len(word) - 1]

    if word in frequency:
        frequency[word] += 1
    else:
        frequency.update({word: 1})
        
print(frequency)
