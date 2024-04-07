import random
y = list(map(str,input().split()))
t1 = []
t2 = []
while (len(y) != 0):
    x = random.choice(y)
    if (len(t1) == len(t2)):
        t1.append(x)
        y.remove(x)
    elif (len(t1) > len(t2)):
        t2.append(x)
        y.remove(x)
print("Team A: ", t1)
print("Team B: ", t2)

