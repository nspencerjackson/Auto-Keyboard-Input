#from pynput.keyboard import Key, Controller
import time
import pyautogui as pag

#keyboard = Controller()

# Functino to move mouse to x, y coordinates
def moveMouse(x, y):
    pag.moveTo(x,y,0.3)

# Function to click the left button of the mouse
def clickMouse():
    pag.click()

# Function to switch to another window
def alt_tab():
    pag.hotkey('alt', 'tab')

def tab():
    pag.press('tab')

def doubleTab():
    tab()
    tab()

def save():
    pag.hotkey('ctrl', 's')

def ent():
    pag.press('enter')

def type_key(inString):
    pag.write(inString, interval=0.000001)

def copy(inX, inY, outX, outY, time):
    if time == 1:
        pag.moveTo(inX, inY, 0.3)
        pag.dragTo(outX, outY, 1)
    pag.hotkey('ctrl', 'c')

def paste():
    pag.hotkey('ctrl', 'v')

def back_to_month(inX, inY):
    moveMouse(inX, inY)
    clickMouse()
