# Addition of Two Lists (Element-wise)
def add_lists(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"Sum of {list1} and {list2} is {add_lists(list1, list2)}")
