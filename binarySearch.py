def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1

    while ( start <= end ):
        mid = start + ( end - start ) // 2
        if (target < arr[mid]):
            end = mid - 1
        elif (target > arr[mid]):
            start = mid + 1
        else:
            return mid
    return -1

def userInput():
    arr = []
    n  = int(input("Enter number of elements: "))
    print("Enter the elements")
    for i in range(0,n):
        element = int(input())
        arr.append(element)
    print(arr)
    target = int(input("Enter the target element: "))

    result = binarySearch(arr,target)
    if(result == -1):
        print("Element not found")
    else:
        print("The element was found at index ", result)

userInput()
