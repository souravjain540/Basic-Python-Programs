'''
THIS IS A DYNAMIC TEXT-TO-SPEECH CONVERTER WHICH CAN ALSO SAVE THE .MP3 FILE IN YOUR SYSTEM 
ALSO HAS MALE AND FEMALE VOICE SUPPORT, CAN CHANGE THE WORDS PER MINUTE AND HAVE LIVE TEXT-TO-SPEECH OUTPUT AS WELL!

Before running this code, do type these commands in command prompt.
    --> pip install pyttsx3

YOU CAN FEED THE DATA USING THE COMMAND PROMPT:
"python text_to_speech.py "YOUR TEXT HERE" --gender SELECT_GENDER(male, female) --output OUTPUT_FILE_NAME.mp3 --rate RATE_NUMBER --disable-live-text"  

FOR EXAMPLE:
    FOR MALE AND HAVE THE LIVE TEXT-TO-SPEECH OUTPUT: 
    ```` python text_to_speech.py "Hello, this is a male voice example." --gender male --output output_male.mp3 ```


    FOR FEMALE AND HAVE THE LIVE TEXT-TO-SPEECH OUTPUT DSIABLED AND GIVE WORDES PER MINUTE RATE VALUE: 
    ```` python text_to_speech.py "Hello, this is a custom example." --gender female --output custom_output.mp3 --rate 150 --disable-live-text" ````

YOU CAN SEE ALL THE COMMANDS BY TYPING THIS IN THE COMMAND PROMPT: "python text_to_speech.py --help"
 
The OUTPUT_FILE_NAME.mp3 file will get saved after the whole text-to-speech live output is completed saved in the same directory as this .py file!
'''


import argparse
import pyttsx3

def text_to_speech(text, gender, output_file, rate, live_text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Select voice based on gender
    if gender == "male":
        selected_voice = voices[0]  # The first voice in the list is typically male
    elif gender == "female":
        selected_voice = voices[1]  # The second voice in the list is typically female
    else:
        print("Invalid gender choice. Using the default voice.")
        selected_voice = None

    if selected_voice:
        engine.setProperty('voice', selected_voice.id)

    # Set the rate of speech
    engine.setProperty('rate', rate)

    if live_text:
        # Say the text
        engine.say(text)
        engine.runAndWait()

    # Save the speech to an output file
    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text to Speech Converter")
    parser.add_argument("text", help="Text to convert to speech")
    parser.add_argument("--gender", choices=["male", "female"], default="male", help="Voice gender (male or female)")
    parser.add_argument("--output", default="output.mp3", help="Output file name")
    parser.add_argument("--rate", type=int, default=200, help="Speech rate (words per minute)")
    parser.add_argument("--disable-live-text", action="store_true", help="Disable live text feature")
    args = parser.parse_args()

    text_to_speech(args.text, args.gender, args.output, args.rate, not args.disable_live_text)
