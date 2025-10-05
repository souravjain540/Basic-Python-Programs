# pigeonhole_sort.py
# Implementation of Pigeonhole Sort in Python

def pigeonhole_sort(arr):
    """
    Function to perform pigeonhole sort on a list of integers.
    Works efficiently when the range of numbers is not too large.
    """
    if not arr:
        return arr  # handle empty list
    
    # Find minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Calculate range (number of pigeonholes needed)
    size = max_val - min_val + 1

    # Create pigeonholes (buckets)
    holes = [0] * size

    # Place each element in its corresponding hole
    for num in arr:
        holes[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_index = 0
    for i in range(size):
        while holes[i] > 0:
            arr[sorted_index] = i + min_val
            sorted_index += 1
            holes[i] -= 1

    return arr


# Example usage
if __name__ == "__main__":
    arr = [8, 3, 2, 7, 4, 6, 8]
    print("Original array:", arr)
    sorted_arr = pigeonhole_sort(arr)
    print("Sorted array:", sorted_arr)
