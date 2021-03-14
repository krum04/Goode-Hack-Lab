# import libaries
import pyautogui
import random
from time import sleep

# as a failsafe, you can drag the mouse up to the top left of the screen to
# break out of a pyautogui script

while True:
    # generate random time between popups in seconds
    randomTime = random.randrange(20,45)
    sleep(randomTime)
    pyautogui.alert(text="Hey Over Here!", title="Hey", button="STOP!")