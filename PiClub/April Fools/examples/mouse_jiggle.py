#import libraries
import pyautogui
import random

# as a failsafe, you can drag the mouse up to the top left of the screen to
# break out of a pyautogui script

while True: 
    # generate random value between -10 and 10 for X and Y
    randomX = random.randrange(-10,10)
    randomY = random.randrange(-10,10)
    # move mouse by random generated X and Y values
    pyautogui.move(randomX,randomY)