def reverseWordSentence(Sentence):
 
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
 

Sentence = "Split Reverse Join"
print(reverseWordSentence(Sentence))
