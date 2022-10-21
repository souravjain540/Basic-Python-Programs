# The selection sort algorithm sorts an array by repeatedly finding the minimum element.
# Time Complexity :  O(n*n)

"""
Algorithm :-
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted
Pseudocode Selection Sort  :-
   list  : array of items
   n     : size of list
   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i

      /* check the element to be minimum */
      for j = i+1 to n
         if list[j] < list[min] then
            min = j;
         end if
      end for
      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for

end procedure
"""


def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


# Created a User-Input Array
alist = input('Enter The Numbers : ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted List: ', end='')
print(alist)