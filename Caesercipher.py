s=input("enter string ")
k=int(input("enter shift "))
ans=''
for i in s:
        p=ord(i)
        if i.isalpha() and i.isupper():
            if p+(k%26) >90:
                
                ans += chr(p + k%26 -26 )
            else:    
                ans += chr(p+k%26)
        elif i.isalpha() and i.islower():
            if p + (k%26) > 122:
                ans += chr((p+ k%26 -26))
            else:
                ans += chr(p+(k%26)) 
        else:
            ans +=chr(p)
print(ans)
