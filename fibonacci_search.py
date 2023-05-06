
def fib_search(ls, val):
    fibM_minus_2=0
    fibM_minus_1=1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(ls):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_2 + fibM_minus_1
        
    index = -1
    while fibM > 1:
        i=min(index + fibM_minus_2,(len(ls)-1))
        if ls[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM -fibM_minus_1
            index=i
        elif ls[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 -fibM_minus_2
            fibM_minus_2 = fibM -fibM_minus_1
        else:
            return i
    if(fibM_minus_1 and index < (len(ls) -1) and ls[index+1] == val):
        return index+1
    return -1

print(fib_search([1,2,3,4,5,6,7,8,9,10,11,13,15],10))


