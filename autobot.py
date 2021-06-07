
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def tryP(zentrum, buchen):
    zentrumPos = 0
    zentrumlink = ""
    continueButton = 0
    if zentrum == "1":
        #zentrumPos = 330 #SB
        zentrumlink = '\\saarbruecken.png'
    if zentrum == "2":
        #zentrumPos = 350 #SLS
        zentrumlink = '\\saarlouis.png'
    if zentrum == "3":
        #zentrumPos = 405 #NK
        zentrumlink = '\\neunkirchen.png'
    if zentrum == "4":
        #zentrumPos = 480 #LB
        zentrumlink = '\\lebach.png'
    if zentrum == "5":
        #zentrumPos = 505 #LBN  
        zentrumlink = '\\lbn.png'
    if zentrum == 0:
        print("Fehler 1")  
        return

    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen(os.getcwd() + '\\screen.png', grayscale=True, confidence=0.8) != None:
            #mousePos([910,zentrumPos])
            #leftClick() #click on place
            if zentrumPos == 0:
                zentrumPos = pyautogui.locateCenterOnScreen(os.getcwd() + zentrumlink, grayscale=True, confidence=0.7)
                print(zentrumPos)
                continueButton = pyautogui.locateCenterOnScreen(os.getcwd() + '\\weiternicht.png', grayscale=True, confidence=0.7)
            else:
                mousePos([zentrumPos.x,zentrumPos.y])
                leftClick() #click on place
                mousePos([continueButton.x,continueButton.y])
                leftClick() #click on weiter
                time.sleep(0.05)
                next

        elif pyautogui.locateOnScreen(os.getcwd() + '\\nothing.png', grayscale=True, confidence=0.8) != None:
            mousePos([950,360])
            leftClick() #click on zurück
            time.sleep(0.05)
            next
        else:

            place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\booking.png', grayscale=True, confidence=0.7)
            if place:
                mousePos([place.x,place.y])
                leftClick() #click on weiter

            place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\date.png', grayscale=True, confidence=0.3)
            if place:
                mousePos([place.x,place.y])
                leftClick() #click on first date
                #time.sleep(0.01)
            else:
                next
            #########
            # if too slow! use this hardcoded click for date!   and comment line 38 to 46
            # mousePos([860,390])
            # leftClick() #click on first date
            # time.sleep(0.01)
            #########
            place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\weiter.png', grayscale=True, confidence=0.8)
            if place:
                mousePos([place.x,place.y])
                leftClick() #click on weiter
                time.sleep(0.01)
            else:
                next
            #########
            # if too slow! use this hardcoded click for weiter!   and comment line 52 to 59
            # mousePos([1050,730]) #bei 5+ Terminen
            ## mousePos([1050,450]) #bei 1 Termin
            # leftClick() #click on weiter
            # time.sleep(0.30)
            #########

            # if the bot is slower and the Termini (sry für no english :D) is booked somehow 
            # place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\booked_error.png', grayscale=True, confidence=0.7)
            # if place:
            #     next
                
                
            place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\booking.png', grayscale=True, confidence=0.7)
            if place:
                mousePos([place.x,place.y])
                leftClick() #click on weiter


            # if buchen == "1":
            #     mousePos([1060,520])
            #     leftClick() #click on buchen
                
            if buchen == "2":
                mousePos([1060,680])
                leftClick() #click on termin verschieben

            if buchen == 0:
                print("Fehler 2")   

            place = pyautogui.locateCenterOnScreen(os.getcwd() + '\\logout.png', grayscale=True, confidence=0.4)
            if place:
                print("i am out")
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
