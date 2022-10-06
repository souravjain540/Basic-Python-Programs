#Implementation of Linear Regression on a randomly generated data

import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from datetime import datetime
from scipy import stats


#GIVEN DATA
slope=0.5
intercept=2
x = []
y = []

random.seed(1)
for i in range(0, 51):
    x.append(i)
    y.append(x[i] * slope +intercept + random.uniform(-1, 1))
    Length = len(x)
plt.figure(1)
plt.scatter(x,y,c='brown')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Figure 1')
plt.show()

#PREDICTION TIME
slope_pred = 0
intercept_pred = 0
LR = 0.2**7*5  
loss = 0
lossdiff = 1
prevloss = 10**5
while (lossdiff > 0.2**6):#lossdiff value can be changed
    sum_slope = 0
    sum_intercept = 0
    for i in range(Length):
        ypred = x[i] * slope_pred + intercept_pred
        sum_slope= sum_slope + (x[i] * (y[i] - ypred))
        sum_intercept = sum_intercept + (y[i] - ypred)
        loss = loss + (y[i] - ypred)**2
    dm = -2 * sum_slope/ Length
    dc = -2 * sum_intercept / Length
    
    loss = loss / Length
    lossdiff = prevloss - loss
    print("Loss: ",lossdiff)
    prevloss = loss
    slope_pred = slope_pred - LR * dm
    intercept_pred = intercept_pred - LR * dc
#PREDICTED VALUES PRINT 
print("ORIGINAL VALUE:-",'%.1f'%slope)
print("PREDICTED VALUE:-",'%.3f'%slope_pred)
print("ORIGINAL VALUE:-",'%.1f'%intercept)
print("PREDICTED VALUE:-",'%.3f'%intercept_pred)

#LINEAR REGRESSOR
ypredict = []
for i in range(Length):
    ypredict.append(x[i] * slope_pred + intercept_pred)
#PLOTTING
plt.ylabel("y")
plt.xlabel("x")
plt.title("LINEAR REGRESSION")
plt.scatter(x, y, c='red', alpha=1)
plt.plot(x, ypredict, c='green')
plt.grid(True)
plt.show()