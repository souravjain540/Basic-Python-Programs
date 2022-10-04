import random
special = ["!","@","#","$","%","^","&","*"]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [1,2,3,4,5,6,7,8,9,0]
print("Enter length of password:")
length = int(input())
print("Enter no of special characters:")
spec = int(input())
rem_char = length-spec
num_num = rem_char//3
num_alpha = rem_char-num_num
L=[]
alpha_list = random.sample(alpha,num_alpha)
num_list = random.sample(num,num_num)
spec_list = random.sample(special,spec)
for i in alpha_list:
    L.append(i)
for i in num_list:
    L.append(i)
for i in spec_list:
    L.append(i)
random.shuffle(L)
password=""
for i in L:
    password +=str(i)
print("your password is :",password)

