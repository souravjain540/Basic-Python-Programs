"""
Write an algorithm to find the frequency of each word in a given text. 
Your algorithm should keep track of each word it encounters and the number 
of times it has appeared. (You can ignore case sensitivity.)
"""

def func(text : str):
    word_array = []
    current_word =""
    word_check =""
    for char in text:
        if char.isalnum():
            current_word +=char
        elif char.isspace():
            if current_word:
                word_array.append(current_word)
                current_word = ""
        elif char in ".,-_*?\;/}]{[&%+^'!":
            if current_word:
                word_array.append(current_word)
                current_word = ""
            word_array.append(char)
    if current_word:
        word_array.append(current_word)
        
        
    for element in set(word_array):
        word_counter =0
        word_check = element
        for j,element in enumerate(word_array):
            if word_check == word_array[j]:
                word_counter+=1
        print_elements =[]
        temp_element = f"{word_check} : {word_counter}"
        print_elements.append(temp_element)
        print(print_elements)
TEXT = """Magnus Carlsen is a chess player. He has become world! champions! many times..."""
func(TEXT)