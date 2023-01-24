# Simple swapping of array elements using two pointer method

def reverse(arr):
    start = 0
    end = len(arr) - 1
    temp = 0

    while( start < end ):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start += 1
        end -= 1

# User input starts
def userInput():
    arr = []
    n  = int(input("Enter number of elements:"))
    print("Enter the elements")
    for i in range(0,n):
        element = int(input())
        arr.append(element)

    print("Array before reversing:", arr)
    reverse(arr)
    print("Array after reversing:", arr)

userInput()
