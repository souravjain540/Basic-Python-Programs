def maximum(numbers):
	
	max = numbers[0]
	for i in range(1,len(numbers)):
		
		if numbers[i]>max:
			max = numbers[i]
	return max

numbers = []
limit = int(input("Enter maximum limit:"))
for i in range(0,limit):
	num = int(input("Enter a number:"))
	numbers.append(num)

print("Maximum number =",maximum(numbers))
