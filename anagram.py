def same_strings(first, second):
    return first == second


def convert_string_to_sorted_list(word):
    list = []
    for i in word:
        list.append(i)

    list.sort()
    return list


def is_anagram(first, second):
    if (len(first) != len(second)):
        return False
    else:
        for i, j in zip(first, second):
            if i != j:
                return False
        return True


firstInput = input("Type a word: ")
secondInput = input("Type another word: ")

firstWord = firstInput.strip()
secondWord = secondInput.strip()

firstList = convert_string_to_sorted_list(firstWord)
secondList = convert_string_to_sorted_list(secondWord)

if (same_strings(firstWord, secondWord)):
    print("The words are not anagrams")
else:
    if (is_anagram(firstList, secondList)):
        print("The words are anagrams")
    else:
        print("The words are not anagrams")
