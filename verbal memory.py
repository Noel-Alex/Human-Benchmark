import pyautogui
import pytesseract
import cv2
import win32api, win32con
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\noela\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

words = []

time.sleep(5)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:
    time.sleep(1)
    iml = pyautogui.screenshot(region=(600, 375, 800, 100))
    iml.save(r"C:\Users\noela\Documents\human benchmark\savedimage.png")
    img = cv2.imread('savedimage.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('Result', img)
    cv2.waitKey(1)
    word = pytesseract.image_to_string(img)
    if word not in words:
        click(1032, 499)
        words.append(word)
    else:
        click(924, 499)
