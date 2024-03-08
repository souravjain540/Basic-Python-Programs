# import the time module
import time

# define the countdown function
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Times up!!')

# input time in minutes
t = input("Enter the time in minutes: ")

# convert minutes to seconds for the countdown
t = int(t) * 60

# function call
countdown(t)
