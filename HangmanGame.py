import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["baboon", "delhi", "adamantium", "dehradun"]
# choosing a random word from the list
word = random.choice(word_list);
print(f"The chosen word is {word}")
blank_list = []

for i in range(len(word)):
    blank_list += "_"
end_game=False
while end_game == False:
    guess = input("Guess a letter\n")

    if guess not in word:
        lives=lives-1
    else:
        for i in range(len(word)):
            if word[i]==guess:
                blank_list[i]=guess

    if lives==0 or "_" not in blank_list:
        end_game=True

    # Clear.clear()
    for i in blank_list:
        print(i,end=" ")
    print(stages[lives])

if(lives==0):print("YOU LOSE!!")
else :print("YOU WON!!")