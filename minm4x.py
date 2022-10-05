

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    print(sum(sorted_arr[:4])," " ,sum(sorted_arr[1:]))
    
    
a=[]
n=5
for i in range(0,n):
   l=int(input())
   a.append(l)
   
miniMaxSum(a)