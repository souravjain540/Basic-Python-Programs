def pigeonhole_sort(arr):
    # Find the minimum and maximum values in the array
    min_val, max_val = min(arr), max(arr)
    
    # Calculate the range of values
    range_size = max_val - min_val + 1
    
    # Create pigeonholes (an array to store counts of each element)
    pigeonholes = [0] * range_size
    
    # Populate pigeonholes with counts of elements
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * pigeonholes[i])
    
    return sorted_arr

# Example usage:
arr = [3, 8, 2, 4, 5, 6, 1, 7]
sorted_arr = pigeonhole_sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
