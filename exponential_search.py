
def binary_search(arr,l,r,x):
    if r >= l:
        mid=l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,1,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    return -1

def exponential_search(arr,n,x):
    if arr[0] == x:
       return 0
    i=1
    while i < n and arr[i] <= x:
        i= i * 2

    return binary_search(arr,i // 2, min(i,n-1),x)


arr=[1,3,5,9,10,14,15,17,21,23,56]
n=len(arr)
x=10
result=exponential_search(arr,n,x)
if result == -1:
    print("Element not found in array.")
else:
    print("Element is present at index %d " % result)

    
