a = int(input("Enter a number upto which x should be printed : "))
for i in range(1, a + 1):
	for j in range(1, 2 * a):
		if j == i or j == 2 * a - i:
			print(i, end="")
		else:
			print(" ", end="")
	print()

for i in range(a-1, 0, -1):
	for j in range(1, 2 * a):
		if j == i or j == 2 * a - i:
			print(i, end="")
		else:
			print(" ", end="")

	print()
