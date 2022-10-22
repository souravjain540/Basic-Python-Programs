p = list(map(int, input().split()))   #Enter the prices of each day

maxProfit = 0
currentMax = 0

for i in reversed(p):
    currentMax = max(currentMax, i)
    profit = currentMax - i
    maxProfit = max(profit, maxProfit)
    
print("Buy stock when price is:", currentMax-maxProfit) #Buying Price
print("Sell stock when price is:", currentMax)          #Selling Price
print("Maximum profit earned:", maxProfit)              #Profit Earned