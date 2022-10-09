def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
n = int(input("Enter number of elements : "))
lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
selectionSort(lst, n)
print('The array after sorting in Ascending Order by selection sort is:')
print(lst)
