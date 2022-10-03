def insertionsort(arr):

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1

        while (j >= 0 and temp < arr[j]):
            arr[j+1] = arr[j]
            j -=1
        
        arr[j+1] = temp


array = [8, 2, 7, 10, 9, 1, 0]  
print("Array before sorting:\n", array)

insertionsort(array)
print("Array after sorting:\n",array)