import os
import os.path
from pathlib import Path

def display(path, level = 0):
    try :
        path = Path(path)    
    except:
        print("Enter right path")
        return 
    k = os.listdir(path)
    for i in k:
        if os.path.isfile(os.path.join(path, i)):
            print("  "*level, "--F--", i)
        elif os.path.isdir(os.path.join(path, i)):
            print("  "*level, "+-D--", i)
            display(os.path.join(path, i), level = level + 1)
        else:
            print(i)
    return 


if __name__ == "__main__":
    print("Enter a path")
    s = input()
    if s == "" : 
        s = os.getcwd()
    l = 0
    display(s, level = 0)
