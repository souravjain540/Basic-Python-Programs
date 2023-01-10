def print_rangoli(size):
    rangoli = []
    l = (size-1)*4+1
    pattern = ""
    for i in range(97+size-1, 96, -1):
      pattern = f"{pattern}-{chr(i)}" if pattern != "" else chr(i)
      leftSide = f"{pattern :->{l//2+1}}"
      rightSide = leftSide[-2::-1]
      rangoli.append(leftSide + rightSide)
      
    print('\n'.join(rangoli))
    print('\n'.join(rangoli[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)