def is_pal(s):
    return s == s[::-1]   

if __name__ == "__main__":
    word = input("Please enter the word of your choice: ") 
    if is_pal(word):
        print("Yes! The word is a palindrome")   
    else:
        print("Oops! The word is not a palindrome")

