# Bifurcation diagram


from cmath import inf
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import matplotlib as mpl
import time
from numba import njit
import multiprocessing 
from multiprocessing import Pool
multiprocessing.cpu_count()
from functools import reduce

from functools import partial



start_time = time.time()


#change these values 
x0=0.1
begin_r=0
end_r=4
step=0.0001



r=np.arange(begin_r,end_r,step)
X=[]
Y=[]
      
@njit
def bif(x0, r):
    N=1000  
    x = np.zeros(len(range(0, N)))
    x[0]=x0
    for i in range(1,N):
       x[i] = r * x[i-1] * (1 - x[i-1]) #logistic map  #logistic with extra parameter

    return (x[-130:])

bif1 = partial(bif,x0)
if __name__ == '__main__':
    # create and configure the process pool
    with Pool(4) as p:
        
        for i,ch in enumerate(p.map(bif1,r,chunksize=2500)) :
            x1=np.ones(len(ch))*r[i]
            X.append(x1)
            Y.append(ch)
    print("--- %s seconds ---" % (time.time() - start_time))

    plt.style.use('dark_background')      
    plt.plot(X,Y, ".w", alpha=1, ms=1.2)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(1920 / 40, 1080 / 40)
    # print("--- %s seconds ---" % (time.time() - start_time))
plt.show()

