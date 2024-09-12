a=input("Enter the name of the person who paid:")
d={a:0}
name={1:a}
c=int(input("Enter how many ppl are there apart from payee:"))
count=2
for i in range(c):
    b=input("enter his/her name one by one and after one click enter:")
    d[b]=0
    name[count]=b
    count+=1

print("The people involved in this are:")
for i in name:
    print(i," : ",name[i])
b=len(name)
print(name)
print(d)
start=input("Do we start?(y/n)")
if start=="n":
    print("You have no other option!")
option=int(input("MENU\nEnter 1 to split the amount equally.\nEnter 2 if the object bought solely belongs to one person\nEnter 3 if the split is varying\nEnter 4 to end\n"))
while(option<4):    
    if option==1:
        money=float(input("Enter the money:"))
        split=money/len(name)
        print("The split per person is ", split)
        for i in d:
            d[i]+=split
        print(" ")
        print(d)
        option=int(input("MENU\nEnter 1 to split the amount equally.\nEnter 2 if the object bought solely belongs to one person\nEnter 3 if the split is varying\nEnter 4 to end\n"))
        continue
    if option==2:
        print("The people:")
        for i in name:
            print(i," : ",name[i])
        value=float(input("Enter the value:"))
        num=float(input("Who does this belong to:"))
        nam=name[num]
        d[nam]+=value
        print(d)
        print("")
        option=int(input("MENU\nEnter 1 to split the amount equally.\nEnter 2 if the object bought solely belongs to one person\nEnter 3 if the split is varying\nEnter 4 to end\n"))
        continue
    if option==3:
        print("The people:")
        for i in name:
            print(i," : ",name[i])
        no=int(input("How many people will this be used by?:"))
        value=float(input("Enter the money:"))
        split=value/no
        for i in range(no):
            ppl=int(input("Type the number of the person who was involved and click enter:"))
            a=name[ppl]
            d[a]+=split
        print(" ")
        print(d)
        option=int(input("MENU\nEnter 1 to split the amount equally.\nEnter 2 if the object bought solely belongs to one person\nEnter 3 if the split is varying\nEnter 4 to end\n"))
        continue
    else:
        break


print("This is the final split of the bill before tax:")
#can include tax if possible, but since there are non terminating decimals, python rounds the numbers and there is no reason to calculate tax for small transactions
print(d)



    
