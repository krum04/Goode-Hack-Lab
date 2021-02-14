# import libraries
import requests
import pyttsx3

# define page URL
pageUrl = 'https://official-joke-api.appspot.com/random_joke'

# initalize engine object for reading our strings outloud
engine = pyttsx3.init()

# define function that will take our string and load and run it into the engine object


def speak(speechString):
    engine.say(speechString)
    engine.runAndWait()


# store response for our url in page_data
page_data = requests.get(pageUrl)

# store the json data from page in the page_parsed variable
page_parsed = page_data.json()

# view our raw json data
print(page_parsed)

# call on the setup and punchline keys and store them as independent variables
setup = page_parsed['setup']
punchline = page_parsed['punchline']

# pass our variables into the speak function and have a chuckle
speak(setup)
speak(punchline)
