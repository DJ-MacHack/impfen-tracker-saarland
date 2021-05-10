
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def tryP():
    #cnt = -1
    while keyboard.is_pressed('q') == False:
        #cnt++
        if pyautogui.locateOnScreen('E:/User/DJ MacHack/Python/impfen-tracker-saarland/screen.png', grayscale=True, confidence=0.8) != None:
            #print("I can see")
            #if cnt % 5 == 1
            mousePos([910,330]) #430 NK 530 Lebach Nacht
            leftClick() #click on place
            mousePos([1050,600])
            leftClick() #click on weiter
            #mousePos([860,290]) #for own clicks
            time.sleep(0.3)
            next
        elif pyautogui.locateOnScreen('E:/User/DJ MacHack/Python/impfen-tracker-saarland/nothing.png', grayscale=True, confidence=0.8) != None:
            #print("I can see Nothing")
            mousePos([950,390])
            leftClick() #click on zurück
            time.sleep(0.3)
            next
        else:
            mousePos([860,515])
            leftClick()
            mousePos([1060,730])
            leftClick()
            time.sleep(0.3)
            mousePos([1060,680])
            leftClick()
            break
            #pic = pyautogui.screenshot(region=(800,365,500,800)) 
            #for x in range(0, width, 5):
            #    for y in range(0, height, 5):
            #        r,g,b = pic.getpixel((x,y))
            #        if (b in range(150, 200)):
            #            mousePos([x+800,y+365])
            #            leftClick() #click on weiter
            #            time.sleep(0.35)
            #            pic = pyautogui.screenshot(region=(920,630,250,200)) 
            #            for x in range(0, width, 5):
            #                for y in range(0, height, 5):
            #                    r,g,b = pic.getpixel((x,y))
            #                    if (b in range(150, 200)):
            #                        mousePos([x+920,y+630])
            #                        leftClick() # click on bestaetigen
            #                        break
            #pic = pyautogui.screenshot(region=(800,365,500,300))
            #width, height = pic.size
            #for x in range(0, width, 5):
            #    for y in range(0, height, 5):
            #        r,g,b = pic.getpixel((x,y))
            #        if (b in range(200, 250)):
            #            mousePos([x+800,y+365])
            #            leftClick()   #click on date
            #            pic = pyautogui.screenshot(region=(800,365,500,800)) 
            #            for x in range(0, width, 5):
            #                for y in range(0, height, 5):
            #                    r,g,b = pic.getpixel((x,y))
            #                    if (b in range(150, 200)):
            #                        mousePos([x+800,y+365])
            #                        leftClick() #click on weiter
            #                        time.sleep(0.3)
            #                        mousePos([1050,520])
            #                        leftClick() # click on bestaetigen
            #                        break


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print("Click.")          #completely optional. But nice for debugging purposes.

def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x
    y = y
    print(x + " " + y)

def main():
    tryP()
 
if __name__ == '__main__':
    main()

#def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
