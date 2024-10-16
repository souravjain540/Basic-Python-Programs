def leap_year(leap_days,year,start,step):
    if year%100==0:
        if year%400==0:
            leap_days=start+1-step
        else:
            leap_days=start-step
    elif year%4==0:
        leap_days=start+1-step
    else:
        leap_days=start-step
    return leap_days
def same_year(d1,d2):
    days=0
    if d1[1]==d2[1]:
        days+=d2[0]-d1[0]
    else:
        days+=d2[0]
        for i in range(d2[1]-1,d1[1],-1):
            if i in months31:
                days+=31
            elif i in months30:
                days+=30
            elif i==2:
                feb_days=0
                days+=leap_year(feb_days,d1[2],28,0)
        if d1[1] in months31:
                days+=31-d1[0]
        elif d1[1] in months30:
                days+=30-d1[0]
        elif d1[1]==2:
            feb_days=0
            days+=leap_year(feb_days,d1[2],28,d1[0])
    return days
months31=[1,3,5,7,8,10,12]
months30=[4,6,9,11]
date1=input('Starting date (dd/mm/yyyy) - ')
date2=input('Ending date (dd/mm/yyyy) - ')
d1=date1.split('/')
d2=date2.split('/')
for i in range(3):
    d1[i]=int(d1[i])
for i in range(3):
    d2[i]=int(d2[i])
days=0
if d1[2]==d2[2]:
    print(same_year(d1,d2))
else:
    for j in range(d2[2],d1[2]+1,-1):
        leap_year_days=0
        days+=leap_year(leap_year_days,j,365,0)
    days+=same_year([1,1,d2[2]],d2)
    days+=same_year(d1,[31,12,d1[2]])+1
    print(days)
                    
        
