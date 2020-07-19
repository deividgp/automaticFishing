import sys, time
import pyautogui
from pynput import keyboard
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener, KeyCode
from tkinter import *

keyboardController = Controller()
counter = 0
xCoor = 0
isActive = False

def get_pressed(event):
    if event == KeyCode.from_char('e'):
        global counter
        counter += 1
            
def get_released(event):
    global xCoor
    global isActive

    if event == KeyCode.from_char('ñ'):
        pyautogui.press('e')
        
    elif event == KeyCode.from_char('a'):
        screen = ImageGrab.grab().load()
        color=screen[xCoor,2]
    elif event == KeyCode.from_char('e') and not isActive:
        global counter

        if counter <= 1:
            
            skip1 = False
            skip2 = False
            counter = 0

            time.sleep(3)
            screen = ImageGrab.grab().load()
            color=screen[xCoor,2]

            if color == (75, 156, 213):
                isActive = True
                screen = ImageGrab.grab().load()
                color=screen[xCoor,2]
                while color != (0, 204, 0):
                    screen = ImageGrab.grab().load()
                    color=screen[xCoor,2]
                    if color==(101, 69, 0):
                        skip1 = True
                        isActive = False
                        break

                if skip1 == False:
                    counter = 0
                    pyautogui.press('e')
                    time.sleep(1)
                    pyautogui.press('r')
                    screen = ImageGrab.grab().load()
                    color1=screen[xCoor,2]
                    color2 = screen[xCoor,30]
                    while(color1 != (101, 69, 0) and color2 != (255, 204, 77)):
                        screen = ImageGrab.grab().load()
                        color1=screen[xCoor,2]
                        color2 = screen[xCoor,30]
                    isActive = False
                    pyautogui.keyDown('e')
                    pyautogui.keyUp('e')
        else:
            counter = 0
        

listener = keyboard.Listener(on_press=get_pressed,on_release=get_released)

if ImageGrab.grab().size == (1366, 768):
    xCoor = 360
elif ImageGrab.grab().size == (1920, 1080):
    xCoor = 500

root = Tk()
root.minsize(150, 75)
root.title("Automatic fishing")
#root.iconphoto(True, PhotoImage(file='salmon.png'))

introLabel = Label(root, text="Welcome to automatic fishing")
instrucLabel = Label(root, text="Make sure to have Provision's Chalutier: Fishing installed on your computer and use windowed fullscreen on ESO")
startButton = Button(root, text="Start", command=listener.start)
#stopButton = Button(root, text="Stop", command=listener.stop)

#introLabel.grid(row = 0, column = 0, columnspan = 1)
#instrucLabel.grid(row = 1, column= 0)
#startButton.grid(row = 2, column = 0)
#stopButton.grid(row = 2, column = 1)

introLabel.pack()
instrucLabel.pack()
startButton.pack()
#stopButton.pack()

root.mainloop()