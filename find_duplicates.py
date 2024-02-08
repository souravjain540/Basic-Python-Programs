def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates
names = ["Usa", "Kampala", "Denver", "Paris", 
         "Uk", "Denver", "Usa", "UK"]
print(find_duplicates(names))
