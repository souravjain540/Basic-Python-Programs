''' find the second largest integer from the given list '''

def max_num(l=[]):
    x = 0
    for i in range(len(l)-1):
         for j in range(len(l)-1):
             if l[i]> x and l[i] < l[j]:
                 x = l[j]
    return x

lst = [1,2,3,0,45,3,4,434,45435,432,343,541,134]
largest = max_num(lst)
new = [y for y in lst if y != largest]
second_largest = max_num(new)
print('second_largest:', second_largest)
