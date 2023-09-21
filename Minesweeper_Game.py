import random

# Generate a random map to start the game.
def randomMap(n, k):

    arr = [[0 for row in range(0,n)] for column in range(0,n)]

    for num in range(0,k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'

        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right

        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left

        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right

        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right

        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left

        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    return arr

# Generate the map for the player.
def playerMap(n):
    arr = [['-' for row in range(0,n)] for column in range(0,n)]
    return arr

# Display the map on the screen.
def showMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

# Check if player has won.
def checkWin(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

# Check if player is willing to continue the game.
def checkContinue(score):
    print("Your score: ", score)
    isContinue = input("Do you want to try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True

# MINESWEEPER GAME
def Game():

    GameStatus = True
    while GameStatus:
        difficulty = input("Select your difficulty (0,1,2):")
        if difficulty.lower() == '0':
            n = 5
            k = 3
        elif difficulty.lower() == '1':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        minesweeper_map = randomMap(n, k)
        player_map = playerMap(n)
        score = 0

        while True:

            if checkWin(player_map) == False:
                print("Enter the cell you want to open :")
                x,y = map(int,input().split())
                x -= 1 # 0 based indexing
                y -=  1 # 0 based indexing
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over!")
                    showMap(minesweeper_map)
                    GameStatus = checkContinue(score)
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    showMap(player_map)
                    score += 1
 
            else:
                showMap(player_map)
                print("Congratulation! You Win!")
                GameStatus = checkContinue(score)
                break

# Main Program
if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        print('\nGoodbye!')