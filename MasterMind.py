"""
This is a number guessing game, where user has to guess a number of certain digits, 
and the system will say how many digits in the input answer exists in the real answer,
and how many of them are at correct postion

Author : Ruhan-Saad-Dave
Creation date : 25th March 2024
"""

import random

class Master_mind:
    '''
    This class handles the game part of the program,
    it creates a random number, 
    check user input format and give hints based on user answer
    '''
    def __init__(self, digit):
        self.digit = digit
    def __generate_new(self):
        '''generates a random number of desired length, default is 2'''
        self.__real_answer = ""
        for _ in range(0,self.digit):
            n = random.randint(0,9)
            n = str(n)
            self.__real_answer += n
        #print(self.real_answer, len(self.real_answer))

    def check_format(self):
        '''
        Checks if the length of user input is equal to the answer length
        or is the input numbers
        '''
        while True:
            ans = input("Enter your guess:")
            if len(ans) != self.digit:
                print(f"Please enter a number of {self.digit} digits")
            elif not ans.isdigit():
                print("Please enter only numbers")
            else: 
                return ans
    
    def play(self):
        '''
        Controls the main game which calls in the other 2 defined function and gives hint to user 
        also checks if the user win or lose
        '''
        self.__generate_new()
        for chance in range(1,11):
            print('_' * 20)
            print("Current trial:", chance,"/10")
            entered_ans = self.check_format()
            #print(entered_ans, len(entered_ans))
            if entered_ans == self.__real_answer:
                print("You win in ", chance , "tries!")
                break
            else:
                self.exist = 0
                self.position = 0
                for i in range(0, self.digit):
                    if entered_ans[i] == self.__real_answer[i]:
                        self.position += 1
                    if entered_ans[i] in self.__real_answer:
                        self.exist += 1
               
                #print("Guessed number:", entered_ans)
                print("Position = ", self.position)
                print("Exist = ", self.exist)
        else:
            print("You lost the game!!!")
            print("The real answer was:", self.__real_answer)

class UserInterface():
    '''
    This class handles the text based interface of the program
    giving user choices of where they can go
    '''
    def __init__(self):
        self.digit = 2
    def main_page(self):
        '''
        the main user interface
        '''
        while True:
            print("Welcome to MasterMind")
            print("Please choose any one option from below")
            print("1 ~ Play")
            print("2 ~ Difficulty")
            print("3 ~ How to play")
            print("4 ~ Exit")
            main_choice = input("Please enter your choice:")

            if main_choice == "1": 
                print("Did you read the how to play section?")
                choice = input("Enter y/n:")
                if choice == "y":
                    game = Master_mind(self.digit)
                    game.play()
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                else:
                    print("\n" * 5)
                    continue
            

            elif main_choice == "2":
                print("Please select one of the following difficulties:")
                print("1 ~ Baby")
                print("2 ~ Easy")
                print("3 ~ Medium")
                print("4 ~ Hard")
                print("5 ~ Very Hard")
                choice = input("Enter your choice:")
                if choice.isdigit():
                    self.digit = int(choice) * 2
                    print("Difficulty has been changed.")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                else:
                    print("Invalid input!!!")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)

            elif main_choice == "3":
                print("Available guides:")
                print("1 ~ Basic rules")
                print("2 ~ Explaination of hints")
                print("3 ~ Purpose of this project")
                print("4 ~ Future updates")
                print("other ~ Exit")
                help_choice = input("Enter your choice:")
                print("\n" * 3)

                if help_choice  == "1":
                    print("You need to guess a number\nwith number of digits depending on your choice,")
                    print("Baby ~ 2 digits")
                    print("Easy ~ 4 digits")
                    print("Medium ~ 6 digits")
                    print("Hard ~ 8 digits")
                    print("Very Hard ~ 10 digits")
                    print()
                    print("The player has 10 chance to guess the number")
                    print("With the help of the hints, User can guess the number")
                    print("If user guess correct within 10 chances, user wins. Else lose")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                elif help_choice == "2":
                    print("The system will compare your answer with the correct answer and give hints")
                    print("Exist ~ Number of digits in input answer that exists in the correct answer")
                    print("Position ~ Number of digits at correct possition")
                    print("Example:")
                    print("Correct answer = 1234\nEntered answer = 5612\nExist = 2, Position = 0")
                    print("Correct answer = 1234\nEntered answer = 1256\nExist = 2, Position = 2")
                    print("Correct answer = 1234\nEntered answer = 1111\nExist = 4, Position = 1")
                    print("Correct answer = 1122\nEntered answer = 2345\nExist = 1, Position = 0")
                    print("Correct answer = 1234\nEntered answer = 5678\nExist = 0, Position = 0")
                    print("Correct answer = 1234\nEntered answer = 1234\nYou win!!!")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                elif help_choice == "3":
                    print("This project is build in order to improve user's logical thinking and critical thinking skills")
                    print("As it requires user to consider all possible options and eliminate information which is not usefull")
                    print("This game originally was used to guess colours, but ive made it such that the user have to guess numbers")
                    print("The game Mastermind was originally introduced by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert in 1970.")
                    print("He originally named the game 'Bulls and Cows' and later changed to 'Mastermind'.")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                elif help_choice == "4":
                    print("Future updates:")
                    print("Will add GUI")
                    print("Will add new gamemode where user have to guess arrangements of alphabets")
                    print("Will add other games and may shift this game into a platform full of other minigames")
                    print("And many more...")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
                else:
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)

            elif main_choice == "4":
                next = input("Are you sure you want to exit? y/n:")
                if next == "y":
                    print("Thanks for playing")
                    break
                else:
                    print("You chose not to exit")
                    next = input("Press ENTER to continue...")
                    print("\n" * 5)
            else:
                print("Invalid input")
                next = input("Press ENTER to continue...")
                print("\n" * 5)

if __name__ == "__main__":
    page = UserInterface()
    page.main_page()


