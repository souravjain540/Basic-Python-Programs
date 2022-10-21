def main():
    sts = str(input("Input: "))
    without_vowels = shorten(sts)
    print("Output: " + without_vowels)

def shorten(word):
    lttr = ""
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            lttr += letter
    return lttr

if __name__ == "__main__":
    main()