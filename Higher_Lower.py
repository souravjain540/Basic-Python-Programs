import random
from os import system


def get_key_q_dict(val):
    for key, value in q_dict.items():
        if val == value:
            return key


def get_key_a_dict(val):
    for key, value in a_dict.items():
        if val == value:
            return key


print("Welcome to higher lower game.")
consent = input("Do you want to play this game(Y/N): ").lower()
if consent == "y":
    q_list = ["Sai Pallavi", "Virat Kohli", "M S Dhoni", "N T R", "Pooja Kannan", "NIT Delhi", "NIT Calicut", "NIT Warangal"]
    q_dict = {"Sai Pallavi": 7600000,
              "Virat Kohli": 255000000,
              "M S Dhoni": 44700000,
              "N T R": 6500000,
              "Pooja Kannan": 287000,
              "NIT Delhi": 1689,
              "NIT Calicut": 3878,
              "NIT Warangal": 5972,
              }
    playing = 1
    score = 0
    while playing != 0:
        if score != 0:
            random_question1 = random_question2
            random_question2 = random.choice(q_list)
            while random_question2 == random_question1 or random_question2 == random_question1_temp:
                random_question2 = random.choice(q_list)
        else:
            random_question1 = random.choice(q_list)
            random_question2 = random.choice(q_list)
            while random_question2 == random_question1:
                random_question2 = random.choice(q_list)
        a_dict = {
            "A": random_question1,
            "B": random_question2
        }
        ans = get_key_a_dict(get_key_q_dict(max(q_dict[random_question1], q_dict[random_question2])))
        print("Who has more followers in instagram?")
        print(f"A: {random_question1}\n(or)\nB: {random_question2}")
        user_ans = input("Enter your answer(A/B): ").upper()
        if user_ans == ans:
            system("cls")
            print("You win this round.")
            score += 1
            print(f"Your score is {score}")
            random_question1_temp = random_question1
        else:
            system("cls")
            print("Game over")
            print(f"Your score is {score}")
            playing = 0
