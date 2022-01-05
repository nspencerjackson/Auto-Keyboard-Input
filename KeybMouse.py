from pynput.keyboard import Key, Controller
import time
import pyautogui as pag

keyboard = Controller()

# Functino to move mouse to x, y coordinates
def moveMouse(x, y):
    pag.moveTo(x,y,0.3)

# Function to click the left button of the mouse
def clickMouse():
    pag.click()
