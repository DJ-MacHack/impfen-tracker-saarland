
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def tryP(zentrum, buchen):
    zentrumPos = 0
    if zentrum == "1":
        zentrumPos = 330 #SB
    if zentrum == "2":
        zentrumPos = 380 #SLS
    if zentrum == "3":
        zentrumPos = 430 #NK
    if zentrum == "4":
        zentrumPos = 480 #LB
    if zentrum == "5":
        zentrumPos = 530 #LBN  
    if zentrum == 0:
        print("Fehler 1")  
        return
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen(os.getcwd() + '\\screen.png', grayscale=True, confidence=0.8) != None:
            mousePos([910,zentrumPos])
            leftClick() #click on place
            mousePos([1050,600])
            leftClick() #click on weiter
            time.sleep(0.33)
            next
        elif pyautogui.locateOnScreen(os.getcwd() + '\\nothing.png', grayscale=True, confidence=0.8) != None:
            mousePos([950,390])
            leftClick() #click on zurück
            time.sleep(0.33)
            next
        else:
            place = pyautogui.locateOnScreen(os.getcwd() + '\\date.png', grayscale=True, confidence=0.3)
            if place:
                place = pyautogui.center(place)
                mousePos([place.x,place.y])
                leftClick() #click on first date
                time.sleep(0.01)
            else:
                next
            #########
            # if too slow! use this hardcoded click for date!   and comment line 38 to 46
            # mousePos([860,390])
            # leftClick() #click on first date
            # time.sleep(0.01)
            #########
            place = pyautogui.locateOnScreen(os.getcwd() + '\\weiter.png', grayscale=True, confidence=0.8)
            if place:
                place = pyautogui.center(place)
                mousePos([place.x,place.y])
                leftClick() #click on weiter
                time.sleep(0.33)
            else:
                next
            #########
            # if too slow! use this hardcoded click for weiter!   and comment line 52 to 59
            # mousePos([1050,730]) #bei 5+ Terminen
            ## mousePos([1050,450]) #bei 1 Termin
            # leftClick() #click on weiter
            # time.sleep(0.33)
            #########    
            if buchen == "1":
                mousePos([1060,520])
                leftClick() #click on buchen
                return
            if buchen == "2":
                mousePos([1060,680])
                leftClick() #click on termin verschieben
                return
            if buchen == 0:
                print("Fehler 2")   
                return 

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x
    y = y
    print(x + " " + y)

def main():
    zentrum = 0 # 1 SB 2 SLS 3 NK 4 LB 5 LBN
    buchen = 0 # 1 neuer Termin 2 umbuchen
    print("Welches Impfzentrum möchten Sie wählen?")
    print("1 Saarbrücken")
    print("2 Saarlouis")
    print("3 Neunkirchen")
    print("4 Lebach")
    print("5 Lebach Nacht")
    zentrum = input("Ihre Wahl: ")
    print("Möchten Sie einen neuen Termin buchen, falls Sie noch keinen haben? - 1")
    print("Möchten Sie einen früheren Termin buchen, drücken Sie dies wenn Sie schon einen Termin haben? - 2")
    buchen = input("Ihre Wahl: ")
    tryP(zentrum, buchen)
 
if __name__ == '__main__':
    main()

#def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
