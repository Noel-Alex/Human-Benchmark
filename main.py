import pyautogui
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
#X: 1532 Y:  567 RGB: 75, 219, 106


def click(x,y):
#    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):
    try:
        if pyautogui.pixel(1532, 567)[0] == 75 and\
                pyautogui.pixel(1532, 567)[1] == 219 and\
                pyautogui.pixel(1532, 567)[2] == 106:
#   if pyautogui.pixel(1532, 567)[0] == 75 and pyautogui.pixel(1532, 567)[1] == 219 and pyautogui.pixel(1532, 567)[2] == 106:
            click(1532, 567)
    except:
        if pyautogui.pixel(1532, 567)[0] == 75 and \
                pyautogui.pixel(1532, 567)[1] == 219 and \
                pyautogui.pixel(1532, 567)[2] == 106:
            click(1532, 567)
            time.sleep(0.01)
            click(1, 2)