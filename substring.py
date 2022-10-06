def substring(str1,n):
    for i in range(0,n):
        for j in range(i+1,n+1):
            # Printing the substrings using slicing
            # Suppose we have str1="Hello" Str1[0:1] will print "H" 
            # Str1[1:2] will print "He"
            # Str1[1:3] will print "Hel"
            # Str1[1:4] will print "Hell"
            # Str1[1:5] will print "Hello"
            # then i will increment i=2
            # Str1[2:3] will print "e"
            # Str1[2:4] will print "el"
            # And So On
            print(str1[i:j])


str1 = input("Enter a String:")
n=len(str1)
substring(str1,n)