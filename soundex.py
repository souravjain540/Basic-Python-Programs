##SOUNDEX ALGORITHM

text = 'AMANMADHUKAR' ##Enter your text here
plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ## This is the plain text
code = '01230120022455012623010202' ## Here I have assigned the code value respective to the alphabet 
l=[] ## Create empty list
l.append(text[0]) ## So first character goes as it is (here it will be A)
for i in range(1,len(text)):   ## Traversing from 1st Index i.e. M to R over here that is the last character
    if(code[plain.index(text[i-1])]!=code[plain.index(text[i])]):  ## Removing Zeroes from the list
        if (code[plain.index(text[i])] != '0'): ## If not zero
            l.append(code[plain.index(text[i])]) ## then append into list       
for i in range(4):  ## Soundex considers only Four characters therefore traversing only four times
        if (len(l)<4):  ## Suppose the Character less than four then we append 0 in last
            l.append('0')
        

print(l) ##printing list
print(''.join(l[:4])) ##lastly merging the list 


## Happy Coding :)