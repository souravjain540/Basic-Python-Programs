k = int(input("Enter maximum number of trades: "))
prices = eval(input("Enter the array of prices: ")) 
n = len(prices)
	
	# Bottom-up DP approach
profit = [[0 for i in range(k + 1)]
            for j in range(n)]

# Profit is zero for the first
# day and for zero transactions
for i in range(1, n):
    
    for j in range(1, k + 1):
        max_so_far = 0
        
        for l in range(i):
            max_so_far = max(max_so_far, prices[i] -
                        prices[l] + profit[l][j - 1])
                        
        profit[i][j] = max(profit[i - 1][j], max_so_far)

print(profit[n - 1][k])