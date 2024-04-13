import time

def time_convert(sec):
    mins=sec//60
    sec=sec%60
    hours=mins//60
    hours=mins%60
    print('Time Elapsed = {}:{}:{}'.format(int(hours),int(mins),int(sec)))

s=input('Press Enter to Start')
start=time.time()

e=input('Press Enter to End')
end=time.time()

elapsed=end-start
time_convert(elapsed)
