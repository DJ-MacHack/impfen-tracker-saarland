from PIL import ImageGrab
import os
import time

from pyautogui import *
import pyautogui
import keyboard
import random
import win32api, win32con

def screenGrab():
    iml = pyautogui.screenshot(region=(800,311,380,300))
    iml.save(os.getcwd() + '\\screen.png', 'PNG')
 
# def browseWeapons():
#     weaponList = ['Saarbrücken','Saarlouis','Neunkirchen','Lebach', 'Impfzentrum Lebach - Nacht-Termine', 'Zurück', 'Weiter']
#     for i in weaponList:    
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOUSEEVENTF_WHEEL,0,0,120)

# def leftClick():
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(.1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#     print "Click."          #completely optional. But nice for debugging purposes.

def main():
    screenGrab()
 
if __name__ == '__main__':
    main()

