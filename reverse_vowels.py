Characters which are not vowels do not change position in string, but all 
vowels (y is not a vowel), reverse their order.

# Examples 
    reverse_vowels("Tomatoes")
    'Temotaos'

    reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'
    
    
   
def reverse_vowels(s):
    
    string = list(s)
    i = 0 
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)
