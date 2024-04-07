'''
 Before running this code, do type these commands in command prompt.
    --> pip install gTTS 
    --> pip install playsound
'''
from gtts import gTTS  
  
from playsound import playsound   
text_val = input("Enter the text which you want to convert: ")  # Example : 'Learn Some Cool and Basic Python Programs here.'  #
  
language = 'en'  
obj = gTTS(text=text_val, lang=language, slow=False)   
obj.save("python.mp3")  # This helps to save our audio file in the existing folder.
  
playsound("python.mp3")  # This runs the audio when you run the program.