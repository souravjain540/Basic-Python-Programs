
def pigeonhole_sort(a): 
	my_min = min(a) 
	my_max = max(a) 
	size = my_max - my_min + 1

	holes = [0] * size 

	for x in a: 
		assert type(x) is int, "integers only please"
		holes[x - my_min] += 1

	i = 0
	for count in range(size): 
		while holes[count] > 0: 
			holes[count] -= 1
			a[i] = count + my_min 
			i += 1
			

a = [8, 3, 2, 7, 4, 6, 8] 
print("Sorted order is : ", end =" ") 

pigeonhole_sort(a) 
		
for i in range(0, len(a)): 
	print(a[i], end =" ")
