# Simple Tic Tac Toe Game in Terminal

from array import *
import random

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

class Game:
    def __init__(self):
        self.winner=''
        self.player=1
    
    def displayBanner(self):
        print(f"\n {'-'*15} TIC-TAC-TOE {'-'*15} \n")
        print(" You are 'X'")
        self.displayBoard()

    def displayBoard(self):
        print("\n",board[0:3],"\n",board[3:6],"\n",board[6:9],"\n")
    
    def playerInput(self):
        self.checkWin()
        print("Enter a free position between 1 & 9: ")
        try:
            position=int(input())
            if position<10 and position>0:
                self.setValue(position)
            else:
                print("Only between 1 and 9")
                self.playerInput()
        except:
            self.playerInput()

    def setValue(self,pos):
        if board[pos-1]==' ':
            if self.player:
                board[pos-1]='X'
                self.displayBoard()
                self.player=0
                self.compPlay()
            else:
                board[pos-1]='O'
                self.displayBoard()
                self.player=1
                self.playerInput()
        else:
            if self.player:
                self.playerInput()
            else:
                self.compPlay()
    
    def compPlay(self):
        position=random.randint(1,9)
        self.setValue(position)

    def checkWin(self):
        if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' \
           or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' \
           or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' \
           or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
            print("Winner is 'X'(You)")
            q = input()
            exit()
 

        if board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' \
           or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' \
           or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' \
           or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
            print("Winner is O")
            q = input()
            exit() 
        
        if ' ' not in board:
            print("Tie")
            q = input()
            exit()


myGame=Game()
myGame.displayBanner()
myGame.playerInput()