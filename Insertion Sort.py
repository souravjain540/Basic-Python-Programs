# Program for Insertion Sort Algorithm
def InsertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] =arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr

arr=[54,23,78,43,98,101,57,28,65]
print(InsertionSort(arr))
