    from heapq import heappop, heappush  
       
     def heapsort(list1):  
         heap = []  
         for ele in list1:  
             heappush(heap, ele)  
       
         sort = []  
       
         # the elements are lift in the heap  
         while heap:  
             sort.append(heappop(heap))  
       
         return sort  
       
     list1 = [27, 21, 55, 15, 60, 4, 11, 17, 2, 87]  
     print(heapsort(list1))  
