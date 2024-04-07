def solve(a, b):
	return (a+b)*(a-b)

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	res = solve(a, b)
	print(res)
