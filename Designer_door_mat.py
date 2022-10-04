pattern = '.|.'
a, b = map(int, input().split()) # 5 < a < 101 and 15 < b < 303

for i in range(1,a,2):
  print((pattern*i).center(b, '-'))
  
print('WELCOME'.center(b,'-'))
  
for i in reversed(range(1,a,2)):
  print((pattern*i).center(b, '-'))