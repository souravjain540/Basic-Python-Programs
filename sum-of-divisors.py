import math
     
def divSum(num) :
   
    result = 0

    i = 2
    while i<= (math.sqrt(num)) :
       
        if (num % i == 0) :
       
            if (i == (num / i)) :
                result = result + i;
            else :
                result = result +  (i + num/i);
        i = i + 1

    return (result + 1);
num = 102
print (divSum(num))