import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random
import subprocess
import datetime
import requests

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Making microphone Ready!..Done")


random_messages = ["How can I assist you today?",
                    "What can I do for you?",
                    "How's your day going?",
                    "What brings you here today?",
                    "Ready to help with whatever you need.",
                    "What can I help you with right now?",
                    "What’s on your mind?",
                    "How can I make your day better?",
                    "Need any assistance today?",
                    "Let’s make things happen. What do you need?"]

random_messages_2 = ["Hi there!",
                    "Hello!",
                    "Greetings!",
                    "What's up?"]

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get voice input
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except sr.RequestError:
        speak("Sorry, the speech recognition service is down")
        return None
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please try again.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return command.lower()


def tell_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke = response.json()
            speak(f"Here's a joke: {joke['setup']} .. {joke['punchline']}")
        else:
            speak("Sorry, couldn't fetch the joke!")
    except Exception as e:
        speak(f"Error: {e}")

def fetch_fun_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            fact = response.json()['text']
            return fact
        else:
            return "Sorry, I couldn't find a fun fact right now."
    except Exception as e:
        return f"Error fetching fun fact: {e}"

assistant_name = "Jarvis"

def change_assistant_name():

    global assistant_name
    speak("What would you like to name me?")
    new_name = take_command()
    if new_name:
        assistant_name = new_name
        speak(f"My new name is {assistant_name}!")

def easter_egg():
    responses = [
        "You found the secret code! Congratulations!",
        "Did you know? I can dance... in my own way, at least!",
        "I see you're curious, good job finding this hidden gem!"
    ]
    speak(random.choice(responses))


def get_greeting():
    current_hour = datetime.datetime.now().hour
    
    if 0 <= current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon!"
    elif 17 <= current_hour < 21:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"

    fun_fact = fetch_fun_fact()
    return f"{greeting} here's a fun fact for you: {fun_fact}"

print(get_greeting())
speak(get_greeting())

# Function to handle commands
def handle_command(command):
    if command is None:
        return

    commands = command.split('and')

    for cmd in commands:
    
        if 'hello' in cmd:

            speak(random.choice(random_messages_2))

        if 'time' in cmd:
            current_time = datetime.datetime.now().strftime('%I:%M %P')
            speak(f"The time is {current_time}")


        elif 'open site' in cmd:
            websites = {
                'youtube': 'https://youtube.com',
                'google': 'https://google.com',
                'github': 'https://github.com',
                'Linkedin': 'https://Linkedin.com'
            }
            speak("Which site would you like to open, sir?")
            command = take_command()
            site = command.split()[-1].lower()  # Assume last word is the site name

            if site in websites:
                speak(f"Opening {site}.")
                webbrowser.open(websites[site])
            else:
                speak(f"Sorry, I don't have {site} in my database.")

        elif 'open notepad' in cmd:
            speak("Opening Notepad")
            os.system('notepad.exe')

        elif 'open music' in cmd:
            speak("opening music sir...")
            music_path = "C:/Users/adity/Music/PairDrop_files_20240813_0043/Tears after the cloudy weather.mp3"
            subprocess.Popen(["start", music_path], shell = True)

        elif 'joke' in command:
            tell_joke()

        elif 'change name' in command:
            change_assistant_name()

        elif 'secret code' in command:
            easter_egg()

        elif 'exit' in command or 'quit' in cmd:
            speak("Goodbye!")
            return False

        else:
            speak("Sorry, I didn't understand that command.")

        return True


# Main function to execute commands
def main():
    get_greeting()
    running = True
    while running:
        command = take_command()
        running = handle_command(command)

if __name__ == "__main__":
    main()
