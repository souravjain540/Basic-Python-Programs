def re(s):
    n=len(s)
    if n<=1 :
        return s
    temp = re(s[1:])
    if s[0]==s[1]:
        return s[0]+"*"+temp
    else:
        return s[0]+temp
 

s= input().strip()
print(re(s))