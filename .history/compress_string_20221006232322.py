def ab(a):
    i=0
    x=''
    while(i<len(a)):
        j=i+1
        c=1
        while j<len(a) and (a[i]==a[j]):
            j+=1
            c+=1
        if c==1:
            x+=a[i]
        else:
            x+=a[i]+str(c)
        i=j
    return x
a=input()
print(ab(a))