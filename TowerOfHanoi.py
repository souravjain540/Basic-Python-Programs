def TowerOfHanoi(Disks, source, temp, destination):  
    if(Disks == 1):  
        print("Move Disk 1 From {} to {}".format(source, destination))  
        return   
    TowerOfHanoi(Disks - 1, source, destination, temp)  
    print("Move Disk {} From {} to {}".format(Disks, source, destination))  
    TowerOfHanoi(Disks - 1, temp, source, destination)  
  
Disks = int(input("Enter Number of Disks: "))

# Source : A, Intermediate : B, Destination : C  
TowerOfHanoi(Disks, 'A', 'B', 'C')