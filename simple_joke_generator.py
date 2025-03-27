# importing the lib to request data from the API
import requests

#this is the api for the joke generator
url = "https://v2.jokeapi.dev/joke/Any"

#here is a request using the requests lib
request = requests.get(url)

#now we make the data in .json
info = request.json()

# if the joke has only one party then we run this statement
if 'joke' in info:
    print(info['joke'])

#if the joke has two parts then we run this statement
elif 'setup' in info and 'delivery' in info:
    print(f"{info['setup']} - {info['delivery']}")