'''
Check a given string is anagram or not using
collection framework.
An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase. For example, "listen" and "silent" are anagrams of each other.
I will solve it making a hashmap using collection framework.
'''
from collections import Counter

def anagram(str1, str2):
    return Counter(str1) == Counter(str2)

# takes inputs from user and checks whether they are anagram or not.
input1 = input("Enter first string: ")
input2 = input("Enter second string: ")	
print(anagram(input1, input2))