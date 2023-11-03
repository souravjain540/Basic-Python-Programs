# alphabetical-sorting.py
# ----------------------------------------------------
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# using the sorted() function
print(sorted(words))

# using the sort() method
words_sorted = words
words_sorted.sort()
print(words_sorted)

# using the reverse=True parameter
print(sorted(words, reverse=True))

# using the bubble sort
for i in range(len(words)):
    for j in range(len(words) - 1):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]
print(words)