import random as rd

num = rd.randint(1, 10)

print("Try to answer the number in 3 tries or less:")
cont = 1
while True:
    try:
        entry = int(input(f"Try {cont}: "))
        break
    except:
        print("Introduce only a number.\n")

while entry != num and cont < 3:
    cont += 1
    print(f"wrong answer, yo have {4 - cont} tries left.\n")
    while True:
        try: 
            entry = int(input(f"Try {cont}:"))
            break
        except:
            print("Introduce only a number.\n")

if entry == num:
    print("\nCongratulatios, you win.")

else:
    print(f"\nYou Lose, the correct answer was {num}.")