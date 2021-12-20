from pynput.keyboard import Key, Controller
import time
import pyautogui as pag

keyboard = Controller()

def moveMouse(x, y):
    pag.moveTo(x,y,0.3)
