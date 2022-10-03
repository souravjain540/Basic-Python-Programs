def make_readable(seconds): 

    seconds = int(seconds) 

    hour = int(seconds/3600)                        
    minute = int(seconds/60) - (hour*60)            
    second = seconds - (minute*60) - (hour*3600)    

    hour = str(hour) if len(str(hour)) > 1 else '0' + str(hour)                
    second = str(second) if len(str(second)) > 1 else '0' + str(second)
    minute = str(minute) if len(str(minute)) > 1 else '0' + str(minute)

    return f"{hour}:{minute}:{second}"   #returns the value

print(make_readable(input('')))
input('')
