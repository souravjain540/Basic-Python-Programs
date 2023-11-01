#Solution for "Migratory Birds" https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures
#Solution by Sanober494

from collections import Counter

def migratoryBirds(arr):  
    birdCounts = Counter(arr)
    maxFrequency = max(birdCounts.values())    
    maxFrequencyBirds = [birdType for birdType, frequency in birdCounts.items() if frequency == maxFrequency]
    
    return min(maxFrequencyBirds)

num=int(input())
Arr=input()
newArr=list(map(int,Arr.split()))
print(migratoryBirds(newArr))  
