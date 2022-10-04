import time
from plyer import notification
print("Enter the Remainder Message:")
msg = input()
print("Enter the mode of time seconds or minutes or hours")
mode  = input()
print("Enter the time left for remainder or time after which remainder should show:")
t = int(input())
if mode == "seconds":
    
        time.sleep(t)
        notification.notify(
            title = "REMAINDER!!!",
            message = msg,
            timeout = 10
        )
        
elif mode == "minutes":
    
        time.sleep(t*60)
        notification.notify(
            title = "REMAINDER!!!",
            message = msg,
            timeout = 10
        )
        
elif mode == "hours":
    
        time.sleep(t*3600)
        notification.notify(
            title = "REMAINDER!!!",
            message = msg,
            timeout = 10
        )
        