# enter number from user
num = float(input('Enter the number : '))
# num = 16
if(num>=0):
  num_square_root = num**0.5
  print('Square root of %0.2f is %0.2f'%(num,num_square_root))
else:
  print('Your input is a negative number')    
