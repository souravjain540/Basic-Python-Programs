"""
Rock, Paper, Scissors Game 
Developer - Krishna Sarathi Ghosh
Twitter - @KAEKrishCodes 
Youtube - Knowledge, Art and Entertainment with Krish   
Github - https://github.com/KrishnaTheCoder756
"""
import tkinter
from PIL import Image, ImageTk
import random
from time import sleep
from tkinter import StringVar


game_list = ['Rock', 'Paper', 'Scissors']

root = tkinter.Tk()
root.minsize(width=944, height=600)
root.maxsize(width=944, height=600)


# Updateable Game Texts
game = tkinter.Label(root, text='Start The Game!', font="Helvetica 20 bold")
game.grid(column=3, row=6, pady=35)
game2 = tkinter.Label(root, text='Click The Start Button', font="Helvetica 15 bold")
game2.grid(column=3, row=7)

            
# IF USER IS ROCK
def rock_checker():
    computer_choice = random.choice(game_list)

    if computer_choice == 'Rock':
        game.config(text="It's a Tie!")
        game2.config(text="Rock hit Rock")
        usr_text2.config(text="Rock: Tie")
        computer_text2.config(text="Rock: Tie")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    elif computer_choice == 'Paper':
        game.config(text="You Lost!")
        game2.config(text="Paper Covers Rock")
        usr_text2.config(text="Rock: Loser")
        computer_text2.config(text="Paper: Winner")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    else:
        game.config(text="You Won!")
        game2.config(text="Rock Breaks Scissors")
        usr_text2.config(text="Rock: Winner")
        computer_text2.config(text="Scissors: Loser")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'


# IF USER IS PAPER
def paper_checker():
    computer_choice = random.choice(game_list)

    if computer_choice == 'Rock':
        game.config(text="You Won!")
        game2.config(text="Paper Covers Rock")
        usr_text2.config(text="Paper: Winner")
        computer_text2.config(text="Rock: Loser")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    elif computer_choice == 'Paper':
        game.config(text="It's a Tie")
        game2.config(text="Paper hit paper")
        usr_text2.config(text="Paper: Tie")
        computer_text2.config(text="Paper: Tie")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    else:
        game.config(text="You Lost!")
        game2.config(text="Scissors Cuts Paper")
        usr_text2.config(text="Paper: Loser")
        computer_text2.config(text="Scissors: Winner")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

def scissors_checker():
    computer_choice = random.choice(game_list)


    if computer_choice == 'Rock':
        game.config(text="You Lost!")
        game2.config(text="Rock breaks Scissors")
        usr_text2.config(text="Scissors: Loser")
        computer_text2.config(text="Rock: Winner")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    elif computer_choice == 'Paper':
        game.config(text="You Won!")
        game2.config(text="Scissor Cuts Paper!")
        usr_text2.config(text="Scissor: Winner")
        computer_text2.config(text="Paper: Loser")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'

    else:
        game.config(text="It's a Tie!")
        game2.config(text="Scissors hit Scissors")
        usr_text2.config(text="Scissors: Tie")
        computer_text2.config(text="Scissors: Tie")

        rock_button['state'] = 'disable'
        paper_button['state'] = 'disable'
        scissors_button['state'] = 'disable'


# User Image
root.title("Rock Paper Scissors By @KrishnaSarathiGhosh")
image = Image.open("GUIRockPaperScissorsKrishna_Images/user.png")
resized_img= image.resize((200,205))
new_image= ImageTk.PhotoImage(resized_img)
usr_img = tkinter.Label(image=new_image)
usr_img.grid(column=1, row=1, padx=20)

# User Name
usr_text = tkinter.Label(text="You", font="Arial 15 bold")
usr_text2 = tkinter.Label(text="", font="Arial 15 bold")
usr_text.grid(column=1, row=2)
usr_text2.grid(column=1, row=3)


# Versus Text
vtxt = tkinter.Label(text="VS", font="Helvetica 30 italic bold")
vtxt.grid(column=3, row=1, padx=86)

# Start game button


# Intro Text
txt = tkinter.Label(text="A game of : ", font="Helvetica 23 bold", fg="Magenta")
txt.grid(column=1, row=4, padx=3, pady=10)


# Buttons For Choosing
rock_button = tkinter.Button(command=rock_checker,text="Rock", font="Helvetica 23 bold", fg="lightblue", bg="grey", activebackground="lightblue", activeforeground="grey")
rock_button.grid(column=2, row=4, padx=5, pady=10)
rock_img = Image.open('GUIRockPaperScissorsKrishna_Images/rock.png')
resized_rock_img = rock_img.resize((80,80))
new_rock_img = ImageTk.PhotoImage(resized_rock_img)
rock_img_2 = tkinter.Label(image=new_rock_img)
rock_img_2.grid(column=2, row=5)

paper_button = tkinter.Button(command=paper_checker,text="Paper", font="Helvetica 23 bold", fg="Green", bg="Yellow", activebackground="Green", activeforeground="Yellow")
paper_button.grid(column=3, row=4,padx=5, pady=10)
paper_img = Image.open('GUIRockPaperScissorsKrishna_Images/paper.jpg')
resized_paper_img = paper_img.resize((80,80))
new_paper_img = ImageTk.PhotoImage(resized_paper_img)
paper_img_2 = tkinter.Label(image=new_paper_img)
paper_img_2.grid(column=3, row=5)

scissors_button = tkinter.Button(command=scissors_checker,text="Scissors", font="Helvetica 23 bold", fg="Red", bg="lightblue", activebackground="Red", activeforeground="lightblue")
scissors_button.grid(column=4, row=4, pady=10, padx=5)
scissors_img = Image.open('GUIRockPaperScissorsKrishna_Images/sc.png')
resized_scissors_img = scissors_img.resize((80,80))
new_scissors_img = ImageTk.PhotoImage(resized_scissors_img)
scissors_img_2 = tkinter.Label(image=new_scissors_img)
scissors_img_2.grid(column=4, row=5)


#Computer Image
image2 = Image.open("GUIRockPaperScissorsKrishna_Images/anyfile.jpg")
photo2 = ImageTk.PhotoImage(image2)
resized_img2= image2.resize((200,205))
new_image2= ImageTk.PhotoImage(resized_img2)
usr_img = tkinter.Label(image=new_image2)
usr_img.grid(column=7, row=1)

# Computer Name
frame = tkinter.Frame(root).grid(column=7, row=2)
computer_text = tkinter.Label(frame, text="Computer", font="Arial 15 bold")
computer_text2 = tkinter.Label(frame, text="", font="Arial 15 bold")
computer_text.grid(column=7, row=2)
computer_text2.grid(column=7, row=3)

rock_button['state'] = 'disable'
paper_button['state'] = 'disable'
scissors_button['state'] = 'disable'

def game1():
    rock_button['state'] = 'active'
    paper_button['state'] = 'active'
    scissors_button['state'] = 'active'

start = tkinter.Button(text="Start Game!", fg="white", bg='blue', activebackground='white', activeforeground='blue', font='Arial 15 bold', command=game1).grid(row=2, column=3)
root.mainloop()
