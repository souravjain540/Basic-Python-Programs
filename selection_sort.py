def selectionsort(arr):
    
    for i in range(len(arr)):
        minimum = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


array = [99, 10, 29, 90, 100, 38, 2938, 23, 498]
print("Array before sorting:\n", array)
selectionsort(array)
print("Array after sorting:\n",array)


