def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = merge_sort(unsorted_list[:middle])
    right_list = merge_sort(unsorted_list[middle:])

    return merge(left_list, right_list)

def merge(left_half, right_half):
    res = []
    i = j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            res.append(left_half[i])
            i += 1
        else:
            res.append(right_half[j])
            j += 1

    res.extend(left_half[i:])
    res.extend(right_half[j:])
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))
