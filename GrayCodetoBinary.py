def flip_num(my_nu):
    return '1' if(my_nu == '0') else '0';

def gray_to_binary(gray):
    binary_code=""
    binary_code += gray[0]
    for i in range(1,len(gray)):

        if (gray[i]=='0'):
            binary_code += binary_code[i-1]
        else:
            binary_code += flip_num(binary_code[i-1])

    return binary_code

# gray_code="01101001"


gray_code=input("please enter the gray code\n")
print("the gray code is : ")
print(gray_code)
# x=gray_to_binary(gray_code)
print("binary code of", gray_code, "is",gray_to_binary(gray_code))              

# for converting binary numb to decimal
value=0
b_num=list(gray_to_binary(gray_code))

for i in range(len(b_num)):
    digit=b_num.pop()
    if digit =='1':
        value = value + pow(2,i)

print("the decimal value of the number is ", value)        


# print(12//5)
