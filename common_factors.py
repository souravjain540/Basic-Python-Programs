factors1 = []
factors2 = []
com_factors = []

def find_factors(num,factors):
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def compare_factors(fac1,fac2,cf):
    for i in fac1:
        for a in fac2:
            if i == a:
                cf.append(i)
    return cf

num1 = int(input(("Enter number 1 ")))
num2 = int(input(("Enter number 2 ")))
find_factors(num1,factors1)
find_factors(num2,factors2)
compare_factors(factors1,factors2,com_factors)
commonfactors = ', '.join(str(i) for i in com_factors)
print ('The common factors of ' + str(num1) + ' and ' + str(num2) + ' are ' + commonfactors)