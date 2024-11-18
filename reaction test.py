from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1532, 567)[0] == 75 and \
            pyautogui.pixel(1532, 567)[1] == 219 and \
            pyautogui.pixel(1532, 567)[2] == 106:
        click(1532, 567)
