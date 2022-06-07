def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     

pa = int(input("Enter the principle amount: "))
time= int(input("Enter the time: "))
roi = int(input("Enter the rate of interest: "))

print(simple_interest(pa, time, roi))
