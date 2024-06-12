"""
Accepts the name of a character
belonging in the A Song of Ice And Fire/Game of Thrones universe
as input then fetches and prints out data about that character
using the public api: 'An API of Ice And Fire'
Link: 'https://anapioficeandfire.com/'
"""
 
import requests
 
 
def get_character_data() -> dict:
    """
    Returns a dictionary containing the data about
    a A Song of Ice And Fire/Game of Thrones character
    """
    while True:
        try:
            character_name = input("Enter a Game of Thrones character's name: ").strip()
            uppercase_first_letters = character_name.title()
            replace_blank = uppercase_first_letters.replace(" ", "%20")
            url = "https://www.anapioficeandfire.com/api/characters?name="
            entire_character_data = requests.get(f"{url}{replace_blank}").json()[0]
 
            if entire_character_data["name"] == uppercase_first_letters:
                print(f"\nThe data on {uppercase_first_letters} is being fetched")
 
                """
                Each of the 'allegiances', 'books', and 'povBooks' keys in the
                dictionary contains an array of resource URLs that leads to more data.
                In order to only get the names of the character's allegiances, books,
                and povBooks, we need to loop through the array while
                using requests.get(). We then replace the URLs in the array with the
                names we just fetch
                """
                for i in range(len(entire_character_data["allegiances"])):
                    allegiances_url = entire_character_data["allegiances"][i]
                    allegiances_name = requests.get(allegiances_url).json()["name"]
                    entire_character_data["allegiances"][i] = allegiances_name
 
                for i in range(len(entire_character_data["books"])):
                    books_url = entire_character_data["books"][i]
                    books_name = requests.get(books_url).json()["name"]
                    entire_character_data["books"][i] = books_name
 
                for i in range(len(entire_character_data["povBooks"])):
                    povBooks_url = entire_character_data["povBooks"][i]
                    povBooks_name = requests.get(povBooks_url).json()["name"]
                    entire_character_data["povBooks"][i] = povBooks_name
 
                return entire_character_data
 
            else:
                raise Exception
 
        except Exception:
            print("Sorry, there's no data on this character.Please check your spelling")
            continue
 
 
if __name__ == "__main__":
    data = get_character_data()
    print(" ")
    for x, y in data.items():
        print(f"{x}: {y}")
