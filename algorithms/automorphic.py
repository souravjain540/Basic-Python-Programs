print("Enter the number you want to check:")  
num=int(input())  
square=num*num    
flag=0   
while(num>0):   
    if(num%10!=square%10):  
        print("No, it is not an automorphic number.")  
        flag=1  
        break                       
       
    num=num//10                        
    square=square//10   
if(flag==0):  
    print("Yes, it is an automorphic number.")  
