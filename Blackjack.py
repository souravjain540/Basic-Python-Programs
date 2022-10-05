logo="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

print(logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

player=[]
computer=[]

player_sum=0
computer_sum=0

player.append(random.choice(cards))


rand = random.choice(cards)
if (rand == 11 and rand + computer_sum > 21):
    player.append(1)
else:
    player.append(rand)


computer.append(random.choice(cards))


randco = random.choice(cards)
if (rand == 11 and rand + computer_sum > 21):
    computer.append(1)
else:
    computer.append(rand)

player_sum+=player[0]+player[1]
computer_sum+=computer[0]+computer[1]

while(player_sum<=21):
    print(f"Your cards : {player} ,current score : {player_sum}")
    print(f"Computer's first card : {computer[0]}")

    accept=input("Type y to get another card , Type n to pass : ")
    if(accept=='y'):
        rand=random.choice(cards)
        if(rand==11 and rand+player_sum>21):
            player_sum+=1
            player.append(1)
        else:
            player_sum+=rand
            player.append(rand)
    else:break

if player_sum>21:
    print(f"Your cards : {player} ,current score : {player_sum}")
    print("You Lost")
    exit()

while computer_sum<player_sum:
    rand=random.choice(cards)
    if (rand == 11 and rand + computer_sum > 21):
        computer_sum += 1
        computer.append(1)
    else:
        computer_sum += rand
        computer.append(rand)

if computer_sum>21 or player_sum>computer_sum :
    print(f"Your cards : {player} ,Your score : {player_sum}")
    print(f"Computer cards : {computer} ,Computer score : {computer_sum}")

    print("You Won")
    exit()
if(computer_sum==player_sum):
    print(f"Your cards : {player} ,Your score : {player_sum}")
    print(f"Computer cards : {computer} ,Computer score : {computer_sum}")

    print("Draw!!")
    exit()

if(computer_sum>player_sum):
    print(f"Your cards : {player} ,Your score : {player_sum}")
    print(f"Computer cards : {computer} ,Computer score : {computer_sum}")

    print("You Lost")
    exit()