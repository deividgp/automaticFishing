import sys, time
import pyautogui
from pynput import keyboard
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener, KeyCode
from tkinter import *

#cd Users/dayd4/Documents/automaticFishing
keyboardController = Controller()
counter = 0

def get_pressed(event):
    if event == KeyCode.from_char('e'):
        global counter
        counter += 1
            
def get_released(event):
    #print('pressed:', event)
    if event == KeyCode.from_char('ñ'):
        pyautogui.press('e')
        
    elif event == KeyCode.from_char('a'):
        screen = ImageGrab.grab().load()
        color=screen[360,2]
        print(ImageGrab.grab().size)
        print(color)
    elif event == KeyCode.from_char('e'):
        global counter

        if counter <= 1:
            skip1 = False
            skip2 = False
            counter = 0

            print("hold pressed: e")
            time.sleep(1)
            print("hi")
            screen = ImageGrab.grab().load()
            color=screen[360,2]
            
            if color == (75, 156, 213):
                print("hi2")
                screen = ImageGrab.grab().load()
                color=screen[360,2]
                while color != (0, 204, 0):
                    screen = ImageGrab.grab().load()
                    color=screen[360,2]
                    print(color)
                    if color==(101, 69, 0):
                        skip1 = True
                        print("hihihihi")
                        break

                if skip1 == False:
                    counter = 0
                    pyautogui.press('e')
                    time.sleep(1)
                    pyautogui.press('r')
                    screen = ImageGrab.grab().load()
                    color1=screen[360,2]
                    color2 = screen[360,30]
                    while(color1 != (101, 69, 0) and color2 != (255, 204, 77)):
                        screen = ImageGrab.grab().load()
                        color1=screen[360,2]
                        color2 = screen[360,30]

                    print(counter)
                    #time.sleep(2)
                    print("hi3")
                    pyautogui.keyDown('e')
                    pyautogui.keyUp('e')
                    time.sleep(1)
        else:
            counter = 0

listener = keyboard.Listener(on_press=get_pressed,on_release=get_released)

root = Tk()
root.minsize(150, 75)
root.title("Automatic fishing")
root.iconphoto(True, PhotoImage(file='salmon.png'))

introLabel = Label(root, text="Welcome to automatic fishing")
instrucLabel = Label(root, text="Make sure to have Provision's Chalutier: Fishing installed on your computer and use windowed fullscreen on ESO")
startButton = Button(root, text="Start", command=listener.start)
stopButton = Button(root, text="Stop", command=listener.stop)

#introLabel.grid(row = 0, column = 0, columnspan = 1)
#instrucLabel.grid(row = 1, column= 0)
#startButton.grid(row = 2, column = 0)
#stopButton.grid(row = 2, column = 1)

introLabel.pack()
instrucLabel.pack()
startButton.pack()
stopButton.pack()

root.mainloop()