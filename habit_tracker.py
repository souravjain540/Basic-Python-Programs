import json
import datetime
habits={
    1:"Drink water",
    2:"Walk the dog",
    3:"Run",
    4:"Read a book"
}

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

x = datetime.datetime.now()
today_date= str(str(x.year)+ "-"+str(x.month) +"-"+ str(x.day))
if today_date not in data:
    data[today_date] = {}

def tracker():
    completed_habits=0
    for habit_id in habits:
        user_answer = input(f"{habits[habit_id]} ? (y/n)").lower()
        habit_name= habits[habit_id]
        if user_answer == "y":
            value = True
            completed_habits +=1
        elif user_answer == "n":
            value = False
        else:
            print("Incorrect input!")
            return
        data[today_date][habit_name] = value
    status= "Amazing job !" if completed_habits == len(habits) else "Keep it going !"
    print(f"You have completed {completed_habits}/{len(habits)} of your habits! {status}")
tracker()
with open('data.json', 'w') as f:       
    json.dump(data, f)