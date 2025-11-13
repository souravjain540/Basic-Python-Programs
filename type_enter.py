#Prompts The User To Type Some Sentence(s) Followd By 'enter'
s=input("Enter Few Sentences:")
l=len(s)
c=0 #Count For Whitespaces
alc=0 #Count For Alphanumeric Characters
for ch in s :
    if ch.isspace():
        c+=1
    elif ch.isalnum():
        alc+=1
'''
Percentage Calculation For Occurence Of
Alphanumeric Characters In The Sentence
'''
alnp=alc/l*100 
print("Original Sentence:")
print(s)
print("Number Of Words:",(c+1))
print("Number Of Character:",l)
print("Alphanumeric Percentage:",alnp,"%")