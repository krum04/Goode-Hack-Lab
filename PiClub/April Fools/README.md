# April Fools Scripts

Sometimes its fun to wield your experience in code for a little mischief. With April 1st come up, now is a great time to get creative with your scripting and come up with some fun scripts. I've highlighted a couple of libraries bellow that are great for just this! See what you can come up with and we will demo our scripts on the big day. Please make sure your script is not going to create any long term damage!

## [Webbrowser](https://docs.python.org/3/library/webbrowser.html)

We won't get into the weeds on this one, but the basic use to open a browser with a specific URL is bellow

```python
import webbrowser
webbrowser.open("bit.ly/hacklabmusic") #Opens your browser to everyone's favorite jam
```



## [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/)

PyAutoGui is the only library that will require a pip install. Enter the command in your terminal bellow to install the library.

> pip3 install pyautogui

Once you can now enter python and import the pyautogui library

```python
import pyautogui
```

Some basic functions in PyAutoGui

## [Mouse Control](https://pyautogui.readthedocs.io/en/latest/mouse.html)

Bellow are some of the basic mouse control functions built into PyAutoGui, make sure to check out the link to a full list of controls outlines in the full documentation

```python
pyautogui.size() #Return the main display size in pixel resolution
pyautogui.position() #Return current mouse possition 

pyautogui.move(x,y) #Move the mouse based on current position, takes an X and Y integer argument
pyautogui.moveTo(x,y) #Move the mouse to a specific location on the screen with an X and Y integerger

pyautogui.click() #Single click the mouse
pyautogui.doubleClick() #Double click the mouse
```

## [Keyboard Control](https://pyautogui.readthedocs.io/en/latest/keyboard.html)

PyAutoGui can also manipulate the keyboard. Bellow is a list of  some of the basic controls, make sure to check out the link to the official documentation to get a full list of functions. 

```python
pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

pyautogui.press('enter')  # press the Enter key
pyautogui.press('f1')     # press the F1 key
pyautogui.press('left')   # press the left arrow key
```

## [Message Box](https://pyautogui.readthedocs.io/en/latest/msgbox.html)

PyAutoGui can create message boxes to allow user to interact with the program. Again check out the complete docs for all the possible functions. 

```python
pyautogui.alert(text='', title='', button='OK') # Creates a pop up allert that will halt your program
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel']) # Creates a pop up with multiple options
```

## [Random](https://docs.python.org/3/library/random.html)

Using the random library can help add some unpredictability to your script! The ***randrange()*** function can be used to generate a random number between a given range. Let's use it with the ***pyautogui.move()*** function to generate some random mouse jitter.

```python 
# import our libraries
import pyautogui
import random

# create a loop with the while True statment
while True:
    # use randrange to generate random x y coordinates that will swing between 20 pixels 
    pyautogui.move(random.randrange(-10,10),random.randrange(-10,10))
```

When you execute this script, your mouse should experience a random jitter effect that might drive you insane if you were not clued into what was going on. 

If we import sleep from the time library, we can generate random pop ups at unpredictable times. Lets write a quick script that will create a pop every 20 - 50 seconds. 

```python
# import our libraries
import pyatuogui
import random
from time import sleep

# create a loop with the while True statement:
while True:
    # the sleep funciton takes a value of seconds, we will want to generate a random number between 20 - 50
    randomTime = random.randrange(20,50)
    sleep(randomTime)
    pyautogui.alert('Hey!', 'Anoying Allert', 'OK')
```

You can get creative with these libraries to create some fun scripts sure to annoy anyone on April fools. Try combining them with some of the other libraries you have used in the past such as the **Pyttsx3** to add some voice to your projects. 
