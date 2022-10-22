def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
                
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
       
        arr[j + 1] = key

arr = [9, 8, 6, 7, 1]
print("Unsorted Array:", arr)
insertion_sort(arr)
print('Sorted Array: ', arr)
