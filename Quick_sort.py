# Quick sort algorithm

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()
    items_greater = []
    items_lower = []
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([3, 5, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))