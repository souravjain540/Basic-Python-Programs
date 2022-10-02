def make_readable(seconds): #Function converts an amount of seconds into hours:minutes:seconds

    seconds = int(seconds) #converts seconds into integer

    hour = int(seconds/3600)                        #Gets hours
    minute = int(seconds/60) - (hour*60)            #Gets remanining minutes
    second = seconds - (minute*60) - (hour*3600)    #Gets remaining seconds

    hour = str(hour) if len(str(hour)) > 1 else '0' + str(hour)                #adds 0 if the hours,minutes or seconds are only one charachter long
    second = str(second) if len(str(second)) > 1 else '0' + str(second)
    minute = str(minute) if len(str(minute)) > 1 else '0' + str(minute)

    return f"{hour}:{minute}:{second}"   #returns the value

print(make_readable(input('')))
input('')
