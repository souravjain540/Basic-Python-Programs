di

def beadsort(input_list):
    return_list = []
    transposed_list= [0] * max(input_list)
    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]

    for i in range(len(input_list)):
        return_list.append(sum(n > i for n in transposed_list))

    return  return_list

input_list=[1,45,77,23,2,78,5,67,4,89]
print(beadsort(input_list))


