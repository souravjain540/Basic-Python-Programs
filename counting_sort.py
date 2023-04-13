
def countSort(array):

    output=[0 for i in range(len(array))]

    count=[0 for i in range(256)]

    ans = ["" for i in array]
                      
    for i in array:
        count[ord(i)] += 1


    for i in range(256):
        count[i]= count[i] + count[i-1]

    for i in range(len(array)):
        output[count[ord(array[i])] -1] = array[i]
        count[ord(array[i])] -= 1


        for i in range(len(array)):
            ans[i] = output[i]

    return ans

if __name__=="__main__":
    array="retributivejustice"
    ans=countSort(array)
    print("Sorted character array is %s" % ("".join(ans)))

    



         

     
        
        
    
