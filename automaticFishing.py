import sys, time, os, pyautogui, ctypes
from pynput import keyboard
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener, KeyCode
from tkinter import *
from tkinter import messagebox

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
        
def getXCoor():
    global xCoor
    if ImageGrab.grab().size == (1366, 768):
        xCoor = 360
    elif ImageGrab.grab().size == (1920, 1080):
        xCoor = 500

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if not isAdmin():
    messagebox.showerror("Error", "You have to run this program as administrator")
else:
    getXCoor()
    listener = keyboard.Listener(on_press=get_pressed,on_release=get_released)

    root = Tk()
    root.minsize(150, 125)
    root.title("Automatic fishing")
    #root.iconphoto(True, PhotoImage(file='salmon.png'))

    Label(root, text="Welcome to automatic fishing").pack()
    Label(root, text="Make sure to have Provision's Chalutier: Fishing installed on your computer use windowed fullscreen on ESO").pack()
    Label(root, text="If this program stops working click on 'Restart' and then on 'Start'").pack()
    Button(root, text="Start", command=listener.start).pack()
    #Button(root, text="Stop", command=listener.stop).pack()
    Button(root, text="Restart", command=restart_program).pack()

    root.mainloop()