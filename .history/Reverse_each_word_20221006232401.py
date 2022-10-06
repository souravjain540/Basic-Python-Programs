def reverseword(s): 
   
   w = s.split(" ")        
                           
   nw= [i[::-1] for i in w]
                          
   ns = " ".join(nw)
   return ns
# Driver's Code 
s = input()
print(reverseword(s))