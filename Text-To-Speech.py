from gtts import gTTS
"""
    Install gTTS : pip3 install gTTS

"""

# Initialize the gTTS object 
file_path = str(input("Enter the File name with Extension : "))
with open(file_path) as f:
    file_text = f.read()
    

lg = input("Enter Language code : ")
tts = gTTS(file_text, lang=lg) 

# Save the audio file
tts.save(file_path.split(".")[0] + ".mp3")


