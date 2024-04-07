def knapsack_recursive(wt,val,W,n):
    if n==0 or W==0:
        return 0
    else:
        if wt[n-1]<=W:
            return max(val[n-1]+knapsack_recursive(wt,val,W-wt[n-1],n-1),knapsack_recursive(wt,val,W,n-1))
        elif wt[n-1]>W:
            return knapsack_recursive(wt,val,W,n-1)
W = 6
wt = [1,2,3,6]
val = [1,2,4,6]
n=4
knapsack_recursive(wt,val,W,n)
            
