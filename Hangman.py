import random

print("Welcome to Hangman.")
print("Description:")
print("In this game, you have to guess the word correct in certain number of attempts or else you lose.")
verbs = ["Analyze", "Create", "Estimate", "Involve", "Respond", "Admit", "Evaluate", "Participate", "Seek",
         "Compensate",
         "Deduct", "Believe", "Link", "Remove", "Commit", "Implement", "Prioritize", "Assess", "Define", "Function",
         "Legislate", "Achieve", "Conclude", "Focus", "Perceive", "Select", "Consent", "Demonstrate", "Illustrate",
         "Locate", "Validate", "Communicate", "Impose", "Survive", "Approach", "Derive", "Confirm", "Occur",
         "Administer", "Conduct",
         "Invest", "Purchase", "Survey", "Constrain", "Demand", "Imply", "Publish", "Specify", "Contrast", "Integrate",
         "Deviate", "Pursue", "Allocate", "Precede", "Lead"]
random_word = "participate"
display = []
for i in range(0, len(random_word)):
    display.append("_")

print(f"The word you have to guess is of {len(random_word)} letters in length.")
guessed_word = ""
for letter in display:
    guessed_word += letter
print(guessed_word)
lives = 6
status = ""
while lives != 0:
    before_word = guessed_word
    user_guess = input("Enter any letter which you think the word might contain: ").lower()
    for i in range(0, len(random_word)):
        if user_guess == random_word[i]:
            # if user_guess in display:
            #     pass
            # else:
            display[i] = random_word[i]
            guessed_word = ""
            for letter in display:
                guessed_word += letter
    # print(guessed_word)
    after_word = guessed_word
    if guessed_word == random_word:
        print("You Win.")
        break
    if after_word == before_word:
        lives -= 1
        print(f"You have {lives} more lives left.")
        if lives == 5:
            print("""                        ________
                        |      |
                        0      |
                               |
                               |
                               |""")
        elif lives == 4:
            print("""                        ________
                        |      |
                        0      |
                        |      |
                               |
                               |""")
        if lives == 3:
            print("""                        ________
                        |      |
                        0      |
                       \|      |
                               |
                               |""")
        if lives == 2:
            print("""                        ________
                        |      |
                        0      |
                       \|/     |
                               |
                               |""")
        if lives == 1:
            print("""                        ________
                        |      |
                        0      |
                       \|/     |
                        |      |
                       /       |""")
    else:
        print(guessed_word)

if lives == 0:
    print("""            ________
            |      |
            0      |
           \|/     |
            |      |
           / \     |""")
    print(f"The correct word is {random_word}.")
    print("You lose.")

