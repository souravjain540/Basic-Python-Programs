###########################################################################

# Question - Arithmetic Progression Generator

# # Develop a program that:
# 1- read the first term and the common difference of a arithmetic progression
# 2- show the first 10 terms of this progression
# 3- ask to user if he wants show some more terms
# 4- finish the program when user says he wants to show 0 terms

###########################################################################

print("Arithmetic Progression Generator")
print("-=" * 50)
first_term = int(input("First term: "))
common_difference = int(input("Common difference: "))
term = first_term
cont = 1
more = 10
total = 0
while more != 0:
    total += more
    while cont <= total:
        print(f"{term}", end=" --> ")
        term += common_difference
        cont += 1

    print("PAUSE.\n")

    more = int(input("How many terms you want to show more? "))
print(f"\n\nArithmetic Progression was finished with {total} terms shown.\n\n")
