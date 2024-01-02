import pygame
import sys
from pygame.locals import QUIT,KEYDOWN
import numpy as np

pygame.init()
# get access to the display system and create a window
# the size of the window is 670x670
screen = pygame.display.set_mode((670,670))
screen_color=[238,154,73]   # set the color of the canvas,[238,154,73] is brown
line_color = [0,0,0]    # set the color of lines，[0,0,0] is black

def check_win(over_pos):    #determine the five pieces are connected
    mp=np.zeros([15,15],dtype=int)
    for val in over_pos:
        x=int((val[0][0]-27)/44)
        y=int((val[0][1]-27)/44)
        if val[1]==white_color:
            mp[x][y]=2  # white pieces
        else:
            mp[x][y]=1  # black pieces

    for i in range(15):
        pos1=[]
        pos2=[]
        for j in range(15):
            if mp[i][j]==1:
                pos1.append([i,j])
            else:
                pos1=[]
            if mp[i][j]==2:
                pos2.append([i,j])
            else:
                pos2=[]
            if len(pos1)>=5:    # five pieces connected
                return [1,pos1]
            if len(pos2)>=5:
                return [2,pos2]

    for j in range(15):
        pos1=[]
        pos2=[]
        for i in range(15):
            if mp[i][j]==1:
                pos1.append([i,j])
            else:
                pos1=[]
            if mp[i][j]==2:
                pos2.append([i,j])
            else:
                pos2=[]
            if len(pos1)>=5:
                return [1,pos1]
            if len(pos2)>=5:
                return [2,pos2]
    for i in range(15):
        for j in range(15):
            pos1=[]
            pos2=[]
            for k in range(15):
                if i+k>=15 or j+k>=15:
                    break
                if mp[i+k][j+k]==1:
                    pos1.append([i+k,j+k])
                else:
                    pos1=[]
                if mp[i+k][j+k]==2:
                    pos2.append([i+k,j+k])
                else:
                    pos2=[]
                if len(pos1)>=5:
                    return [1,pos1]
                if len(pos2)>=5:
                    return [2,pos2]
    for i in range(15):
        for j in range(15):
            pos1=[]
            pos2=[]
            for k in range(15):
                if i+k>=15 or j-k<0:
                    break
                if mp[i+k][j-k]==1:
                    pos1.append([i+k,j-k])
                else:
                    pos1=[]
                if mp[i+k][j-k]==2:
                    pos2.append([i+k,j-k])
                else:
                    pos2=[]
                if len(pos1)>=5:
                    return [1,pos1]
                if len(pos2)>=5:
                    return [2,pos2]
    return [0,[]]

def find_pos(x,y):  # find a place
    for i in range(27,670,44):
        for j in range(27,670,44):
            L1=i-22
            L2=i+22
            R1=j-22
            R2=j+22
            if x>=L1 and x<=L2 and y>=R1 and y<=R2:
                return i,j
    return x,y

def check_over_pos(x,y,over_pos):   # check if the place has a piece
    for val in over_pos:
        if val[0][0]==x and val[0][1]==y:
            return False
    return True # no pieces
flag=False
tim=0

over_pos=[] #  already has a piece
white_color=[255,255,255]   # the color of white pieces
black_color=[0,0,0] # the color of black pieces

while True: # refresh the canvas

    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill(screen_color)   # clean the window
    for i in range(27,670,44):
        # vertical line first
        if i==27 or i==670-27:
            pygame.draw.line(screen,line_color,[i,27],[i,670-27],4)
        else:
            pygame.draw.line(screen,line_color,[i,27],[i,670-27],2)
        # then horizontal line
        if i==27 or i==670-27:
            pygame.draw.line(screen,line_color,[27,i],[670-27,i],4)
        else:
            pygame.draw.line(screen,line_color,[27,i],[670-27,i],2)

    # the point in the center
    pygame.draw.circle(screen, line_color,[27+44*7,27+44*7], 8,0)

    for val in over_pos:    # show all the pieces
        pygame.draw.circle(screen, val[1],val[0], 20,0)

    # if there are five pieces connected
    res=check_win(over_pos)
    if res[0]!=0:
        for pos in res[1]:
            pygame.draw.rect(screen,[238,48,167],[pos[0]*44+27-22,pos[1]*44+27-22,44,44],2,1)
            pygame.display.update() # refresh
        continue    # ggame over
    # obtain the place of mouse
    x,y = pygame.mouse.get_pos()

    x,y=find_pos(x,y)
    if check_over_pos(x,y,over_pos):
        pygame.draw.rect(screen,[0 ,229 ,238 ],[x-22,y-22,44,44],2,1)

    keys_pressed = pygame.mouse.get_pressed()

    if keys_pressed[0] and tim==0:
        flag=True
        if check_over_pos(x,y,over_pos):
            if len(over_pos)%2==0:  # blace pieces
                over_pos.append([[x,y],black_color])
            else:
                over_pos.append([[x,y],white_color])

    if flag:
        tim+=1
    if tim%50==0:
        flag=False
        tim=0

    pygame.display.update()
