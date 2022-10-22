import tkinter as tk
from functools import partial
import time

gui=tk.Tk()
gui.geometry('500x200')
gui.title('Tic Tac Toe')

movesPlayed=[]
game_over=False

Xcount=0
Ocount=0
player,turn=1,'x'

def clicked(obj):
    global player,turn,Xcount,Ocount
    
    button_clicked=''.join(obj.split())
    #row,column=obj.split()
    #row=row.split('w')[1]
    
    
    if button_clicked not in movesPlayed:
        globals()[button_clicked].configure(text=turn.center(6))
        movesPlayed.append(button_clicked)
        globals()[button_clicked]['state']='disabled'
        if player==1:
            player,turn=2,'0'
            Xcount+=1
            player_data.configure(text='Player-2(0) chance')
            
            
        else:
            player,turn=1,'x'
            Ocount+=1
            player_data.configure(text='Player-1(x) chance')
        
        win_check()
    else:
        print('Move already played')

def finish(string):
    global game_over
    game_over=True
    player_data.configure(text='')
    player_win.configure(text=string)
    player_win.pack()
    for i in ('row1','row2','row3'):
        for j in range(3):      
            globals()[i+str(j+1)]['state']='disabled'
    rtry=tk.Button(gui,text='Retry',command=Retry)
    rtry.pack()
    finish.rtry=rtry
            
def Retry():
    global movesPlayed,player,turn,Xcount,Ocount,rtry
    movesPlayed=[]
    player,turn=1,'x'
    Xcount,Ocount=0,0
    for i in ('row1','row2','row3'):
        for j in range(3):
            
            globals()[i+str(j+1)].configure(text=f'       ')
            globals()[i+str(j+1)]['state']='active'
    finish.rtry.pack_forget()
    player_win.pack_forget()
    player_data.configure(text='Player-1(x) chance')
        
def win_check():
    
        
        
    
    if (row11['text'] == row12['text'] == row13['text'] != '       ' or
        row21['text'] == row22['text'] == row23['text'] != '       ' or
        row31['text'] == row32['text'] == row33['text'] != '       ' or
        row11['text'] == row21['text'] == row31['text'] != '       ' or
        row12['text'] == row22['text'] == row32['text'] != '       ' or
        row13['text'] == row23['text'] == row33['text'] != '       ' or
        row11['text'] == row22['text'] == row33['text'] != '       ' or
        row13['text'] == row22['text'] == row31['text'] != '       '
        ):
        
        
        if Xcount>Ocount:
            string='Player 1(X) won'
        else:
            string='Player 2(O) won'
        finish(string)
        
    if not game_over:
        if (Xcount==5 and Ocount==4 or
                Xcount==4 and Ocount==5):
            finish('Draw match')
tk.Label(gui,text="PLAYER-1=X\nPLAYER-2=0").pack()
player_data=tk.Label(gui,text='Player-1(x) chance')
player_data.pack()

row1=tk.Frame(gui)
row1.pack()
row2=tk.Frame(gui)
row2.pack()
row3=tk.Frame(gui)
row3.pack()

player_win=tk.Label(gui,text='')
for i in ('row1','row2','row3'):
    for j in range(3):
        
        vars()[i+str(j+1)]=tk.Button(vars()[i], text=f'       ',bd='1',command=partial(clicked,i+' '+str(j+1)))
        vars()[i+str(j+1)].pack(side='left')


gui.mainloop()
