'''The MIT License (MIT)

Copyright (c) 2023 Lubin Wan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''


import pygame as pg
class Chessboard:                                    # set up the chessboard
    def __init__(s):
        s.grid_lenght = 26                           # the length of chessboard grid
        s.grid_count = 20                            # number of grid
        s.start_x = 150                              # initialize coordinates
        s.start_y = 50
        s.edge_lenght = s.grid_lenght / 2            # edge length


        s.piece = "black"
        s.winner = None
        s.gameover = False
        s.grid = []
        for i in range(s.grid_count):                # the board size is 20*20 grids
            s.grid.append(list("." * s.grid_count))




    def handle_event(s, e):
        origin_x = s.start_x - s.edge_lenght
        origin_y = s.start_y - s.edge_lenght
        chessboard_lenght = (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2
        mouse_pos = e.pos                           # mouse position in the chessboard coordinates
        if (mouse_pos[0] > origin_x and mouse_pos[0] <= origin_x + chessboard_lenght) and (
                mouse_pos[1] >= origin_y and mouse_pos[1] <= origin_y + chessboard_lenght):
            if not s.gameover:
                x = mouse_pos[0] - origin_x          # X direction distance
                c = int(x / s.grid_lenght)
                y = mouse_pos[1] - origin_y
                r = int(y / s.grid_lenght)           # Y direction distance
                if s.set_piece(r, c):
                    s.check_win(r, c)


    def set_piece(s, r, c):
        if s.grid[r][c] == ".":                     # Confirm no piece in this position
            s.grid[r][c] = s.piece
            if s.piece == "black":                  # alternate chess pieces
                s.piece = "white"
            else:
                s.piece = "black"
            return True
        return False


    def check_win(s, r, c):
        n_count = s.get_continuous_count(r, c, -1, 0)
        s_count = s.get_continuous_count(r, c, 1, 0)
        w_count = s.get_continuous_count(r, c, 0, -1)
        e_count = s.get_continuous_count(r, c, 0, 1)
        nw_count = s.get_continuous_count(r, c, -1, -1)
        ne_count = s.get_continuous_count(r, c, -1, 1)
        sw_count = s.get_continuous_count(r, c, 1, -1)
        se_count = s.get_continuous_count(r, c, 1, 1)
        if (n_count + s_count + 1 >= 5) or (e_count + w_count + 1 >= 5) or (se_count + nw_count + 1 >= 5) or (
                ne_count + sw_count + 1 >= 5):
            s.winner = s.grid[r][c]
            s.gameover = True


    def get_continuous_count(s, r, c, dr, dc):      # Count the number of pieces of the same color in one direction
        piece = s.grid[r][c]
        result = 0
        i = 1
        while True:
            new_r = r + dr * i
            new_c = c + dc * i
            if 0 <= new_r < s.grid_count and 0 <= new_c < s.grid_count:
                if s.grid[new_r][new_c] == piece:
                    result += 1
                else:
                    break
            else:
                break
            i += 1
        return result


    def draw(s, screen):
        pg.draw.rect(screen, (185, 122, 87), [s.start_x - s.edge_lenght, s.start_y - s.edge_lenght,           # draw chessboard
                                              (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2,
                                              (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2], 0)
        for r in range(s.grid_count):
            y=s.start_y+r*s.grid_lenght
            pg.draw.line(screen,(0,0,0),[s.start_x,y],[s.start_x+s.grid_lenght*(s.grid_count-1),y],2)
        for c in range(s.grid_count):
            x = s.start_x+c*s.grid_lenght
            pg.draw.line(screen, (0, 0, 0), [x,s.start_y], [x,s.start_y + s.grid_lenght * (s.grid_count - 1)], 2)
        for r in range(s.grid_count):
            for c in range(s.grid_count):
                piece=s.grid[r][c]
                if piece!=".":
                    if piece=="black":                                                # set the color of the pieces
                        color=(0,0,0)
                    else:
                        color=(255,255,255)
                    x=s.start_x+c*s.grid_lenght
                    y=s.start_y+r*s.grid_lenght
                    pg.draw.circle(screen,color,[x,y],s.grid_lenght//2)               # draw pieces
class Gomoku:
    def __init__(s):
        pg.init()
        s.screen=pg.display.set_mode((800,600))
        pg.display.set_caption("五子棋对战")
        s.clock=pg.time.Clock()
        s.font=pg.font.Font(u"C:\Windows\Fonts\Candarab.ttf", 24)
        s.going=True
        s.chessboard=Chessboard()
    def loop(s):                                 # loop
        while s.going:
            s.update()
            s.draw()
            s.clock.tick(50)
        pg.quit()
    def update(s):                               # update screen
        for e in pg.event.get():
            if e.type==pg.QUIT:
                s.going=False
            elif e.type==pg.MOUSEBUTTONDOWN:
                s.chessboard.handle_event(e)
    def draw(s):
        s.screen.fill((255,255,255))
        s.screen.blit(s.font.render("FPS:{0:.2F}".format(s.clock.get_fps()),True,(0,0,0)),(10,10))
        s.chessboard.draw(s.screen)               # draw chessboard window
        if s.chessboard.gameover:
            s.screen.blit(s.font.render("{0}Win".format("black"if s.chessboard.winner=="black"else"white"),True,(0,0,0)),(500,10))
        pg.display.update()                       # update interface
if __name__=="__main__":
    game=Gomoku()
    game.loop()
    
    
    
  ''' # readme_Gomoku_game

The small game I want to make is called Gomoku. It is a very simple chess game.
The two sides of the chess are black and white. When one of the chess pieces is connected to 5 pieces. win.
This game is a two-player battle game. people use the mouse to play chess.
Human-computer battle is not supported, and they cannot regret chess.


First , l start to set up the chessboard. I will explain the size, number and location of the chessboard in the comments.


After setting up the chessboard, I will set the color of the chess pieces so that both sides play chess alternately.


Then set up the winning and losing mechanism to judge the game.
When there is a side with 5 players in a line, it is a victory, and the game is over when one side wins.'''
