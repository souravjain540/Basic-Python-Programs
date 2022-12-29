# Python Program for implementation of
# Recursive Bubble sort and Half Way Bubble Sort
import time


class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x)
                        for x in self.array])

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length
        count = 0

        # Base case
        if n == 1:
            return
        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i +
                                          1] = self.array[i + 1], self.array[i]
                count = count + 1

        # Check if any recursion happens or not
          # If any recursion is not happen then return
        if (count == 0):
            return

        # Largest element is fixed,
        #  recur for remaining array
        self.bubbleSortRecursive(n - 1)

    def bubblesort(self):
        swapped = False
        # Looping from size of array from last index[-1] to index [0]
        for n in range(self.length - 1, 0, -1):
            for i in range(n):
                if self.array[i] > self.array[i + 1]:
                    swapped = True
                    # swapping data if the element is less than next element in the array
                    self.array[i], self.array[i +
                                              1] = self.array[i + 1], self.array[i]
            if not swapped:
                # exiting the function if we didn't make a single swap
                # meaning that the array is already sorted.
                return

# Driver Code


def main():
    array = [64, 34, 25, 12, 22, 11, 90]

    sort = BubbleSort(array)

    # wait for 3 seconds
    time.sleep(3)
    # get the start time
    st = time.time()
    sort.bubbleSortRecursive()
    # get the end time
    et = time.time()
    print("Sorted array using recursive method:\n", sort)
    print("Execution time:", (et-st)*1000, "milliseconds.")

    # wait for 3 seconds
    time.sleep(3)
    # get the start time
    st = time.time()
    sort.bubblesort()
    # get the end time
    et = time.time()
    print("Sorted array using half way method:\n", sort)
    print("Execution time:", (et-st)*1000, "milliseconds.")

# Tests ('pip install pytest'; run with 'pytest Bubble_Sort.py')


def test_result_in_order():
    array = [64, 34, 25, 12, 22, 11, 90]
    sort = BubbleSort(array)
    sort.bubbleSortRecursive()
    for i in range(sort.length-1):
        assert sort.array[i] < sort.array[i+1]


def test_result_in_order_halfway():
    array = [64, 34, 25, 12, 22, 11, 90]
    sort = BubbleSort(array)
    sort.bubblesort()
    for i in range(sort.length-1):
        assert sort.array[i] < sort.array[i+1]


if __name__ == "__main__":
    main()
