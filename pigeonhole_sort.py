
def pigeonhole_sort(array):
    my_min=min(array)
    my_max=max(array)
    size=my_max - my_min + 1

    holes=[0] * size

    for x in array:
        assert type(x) is int,"integers only please"
        holes[x - my_min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + my_min
            i += 1

a=[2,1,7,5,93,67,34,21]
print("Sorted order is ",end= " ")
pigeonhole_sort(a)
for i in range(0,len(a)):
    print(a[i],end=" ")
    
               
        
