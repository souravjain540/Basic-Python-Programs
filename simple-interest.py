def simple_interest(p,t,r):
print('\nThe principal is', p ,
      '\nThe time period is', t,
      '\nThe rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('\nThe Simple Interest is', si)
    return si     

pa = int(input("Enter the principle amount: "))
time= int(input("Enter the time: "))
roi = int(input("Enter the rate of interest: "))

print(simple_interest(pa, time, roi))
