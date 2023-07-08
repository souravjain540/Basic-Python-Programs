# Python script to find a given number in a sorted list using binary search
# The algoritem splits the list in half and checks if the value in the middle
# equals the given number, if it isnt, continuing with the first half of the list
# otherwise continuing with the second half


# Public function which calls a private function with extra parameters.
def find_number(num,lst):
    return __find_number(num,lst,len(lst)-1,0)

# Private function
def __find_number(num,lst,high,low):
    
    # Base case 
    if high >= low:
        
        # Setting mid as the middle index of the list
        mid = (high+low)//2
        
        # The element in index mid equals our number? YAY we found it!
        if lst[mid] == num:
            return mid
        
        # The element is greater than our number - we passed it, it should be on the other half of the list.
        elif lst[mid] > num:
            # Indexing the list to start from to the mid
            return __find_number(num,lst,mid-1,low)
        else:
            # Indexing the list from the mid to high
            return __find_number(num,lst,high,mid+1)
    
    # Couldnt find the number!
    else:
        return -1


# Main
if __name__ == "__main__":
    
    lst= [1,2,3,5,6,7,10,15]
    print(find_number(10,lst))
