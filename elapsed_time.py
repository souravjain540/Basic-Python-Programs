#Measure The Elapsed Time 
#importing time module
import time
#Records the current time
start=time.time()
'''
The loop runs from 0 to 9 taking some time 
in each iteration.
'''
for i in range(0,10):
    print(i)
#The execution is paused for 5 seconds
time.sleep(5)
#records the ending time 
end=time.time()
#Elapsed time= Start Time-End Time
print(f'Elapsed Time :{end-start:.3f} seconds')