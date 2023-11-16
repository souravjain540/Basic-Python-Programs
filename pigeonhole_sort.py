def pigeonhole_sort(arr):
    # Find the minimum and maximum values in arr
    my_min = min(arr)
    my_max = max(arr)
    size = my_max - my_min + 1

    # Create a list, each initially empty
    lst = [0] * size

    # Populate the list
    for x in arr:
        assert type(x) is int, "Integers only please"
        lst[x - my_min] += 1

    # Put the elements back into the array in order
    i = 0
    for count in range(size):
        while lst[count] > 0:
            lst[count] -= 1
            arr[i] = count + my_min
            i += 1
            
arr = [18, 3, 2, 7, 4, 6, 8]
print("Original array:", arr)
pigeonhole_sort(arr)
print("Sorted array:", arr)
