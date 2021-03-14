#import libraries
import webbrowser
import pyautogui
from time import sleep
import random

# launch webbrowser to everyone's favorite song
webbrowser.open('bit.ly/hacklabmusic')
sleep(1)

# f11 to fullpapge browser
pyautogui.press('f11')
sleep(3)

# fullscreen youtube video
pyautogui.press('f')