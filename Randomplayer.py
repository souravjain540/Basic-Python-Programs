import random

class Player:
    def __init__(self, name, sport, age, country):
        self.name = name
        self.sport = sport
        self.age = age
        self.country = country

def generate_random_player():
    sports = ["Football", "Basketball", "Tennis", "Cricket", "Golf", "Swimming", "Athletics"]
    countries = ["USA", "Brazil", "Spain", "Germany", "France", "China", "Russia", "India", "Australia", "Japan"]
    first_names = ["John", "Michael", "David", "James", "Robert", "Maria", "Luisa", "Anna", "Daniel", "Sophia"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Martinez", "Lopez", "Lee", "Kim"]

    name = random.choice(first_names) + " " + random.choice(last_names)
    sport = random.choice(sports)
    age = random.randint(18, 40)
    country = random.choice(countries)

    return Player(name, sport, age, country)

if __name__ == "__main__":
    num_players = 5

    print("Randomly Generated Sport Players:")
    for i in range(num_players):
        player = generate_random_player()
        print(f"Player {i+1}: {player.name}, {player.sport}, {player.age} years old, from {player.country}")
