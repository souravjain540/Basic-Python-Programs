# Create a recursive function called tower of Hanoi and pass two arguments:
# the number of discs n and the names of the rods
# such as source, aux, and destination.

def Towers_Of_Hanoi(numdisks, frm_disc, to_disc, aux_disc):
  # When the number of discs is one, we can define the base case. Simply move the
  # single disc from source to target and return in this scenario.
    if numdisks == 1:
        print("Move disk [1] from rod [",
              frm_disc, "] to rod {", to_disc, '}')
        return
    # Now, use the target as the auxiliary to
    # shift the remaining n-1 discs from source to auxiliary.
    Towers_Of_Hanoi(numdisks-1, frm_disc, aux_disc, to_disc)
    # The remaining 1 disc then moves from source to target.

    # Use the source as the auxiliary to move the n-1 discs on the auxiliary to the target.
    print("Move disk ["+str(numdisks) + "] from rod [",
          str(frm_disc)+" ] to rod {", to_disc, '}')
    Towers_Of_Hanoi(numdisks-1, aux_disc, to_disc, frm_disc)


# Give the number of discs as user input using
# the int(input()) function which converts the string to an integer.
# Store it in a variable.
numdisks = int(input('Enter some random number of disks = '))
# passing the given number of disks as argument to the towers of hanoi recursive function .
Towers_Of_Hanoi(numdisks, 'A', 'C', 'B')
