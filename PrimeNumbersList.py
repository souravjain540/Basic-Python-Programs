#This is a function that returns the list of all prime numbers less than max
#The max will be the maximum value that the prime numbers will have on the list
def find_prime_numbers_up_to_max_number(max):
  #List_of_all_numbers is the list of all natural numbers up to max
  list_of_all_numbers = list(range(2,max+1))
  #Secondary is the copy of all numbers that 
  #will be refined until we only get prime numbers
  secondary_all_numbers = list_of_all_numbers
  length_of_list = len(list_of_all_numbers)
  last_number_on_list = list_of_all_numbers[-1]
  #This is used to find non-prime numbers that will be deleted from secondary_all_numbers
  new_num_list = []

  #i is the current prime number that will be multiplied to find non-prime numbers
  i = 2
  #Index will help find the next prime number
  index = 0
  #We will have two loops. The first while loop keeps track of prime numbers
  while i < secondary_all_numbers[-1]:
    last_number_on_list = secondary_all_numbers[-1]
    #We need to find how many non-prime can be drived from the current prime number
    number = last_number_on_list//i
    #The second loop is a for loop to find all multiples of current prime(multiple of prime is non-prime) 
    for j in range(2,number+1):
      #multiplying the prime to get a list of non-prime numbers
      new_num = i * j
      new_num_list.append(new_num)
    #Now we take out all the non-prime numbers from the list of numbers we have
    secondary_all_numbers = [x for x in secondary_all_numbers if x not in new_num_list]
    #We now find the next prime number on the list of numbers we have
    index += 1
    i = secondary_all_numbers[index]
    new_num_list=[]
    #When the list of refined numbers in this loop does not change from the last loop,
    #We break the loops. We have only primes left on the list.
    if list_of_all_numbers == secondary_all_numbers:
      length_of_list = len(list_of_all_numbers)
      break
    else:
      length_of_list = len(list_of_all_numbers)
  return secondary_all_numbers

max = 98
print(find_prime_numbers_up_to_max_number(max))