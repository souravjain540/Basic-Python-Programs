#this program is made with the purpose of being given a youtube link or a youtube search and open up the requested video
import pywhatkit
#we are using the pywhatkit library link:https://pypi.org/project/pywhatkit/
print("Hello")
#Here we ask the user to give the link 
vid=input("Give me the link or the name of the video you want to watch!\n")
#First we ask for the name of the video or the link and then we input that inside a variable named vid 
try:
    print("Your video is loading...")
    pywhatkit.playonyt(vid)
#Using the pywhatkit.playonyt function we are able to
except:
    print("There was an error with your network:(")
    print("Check your internet conncetion and try again!")
#the try: except: helps us with the possibility of no internet connection being available to the user    
