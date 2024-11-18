import pyautogui
import pytesseract
import cv2
import win32api, win32con
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\noela\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

time.sleep(5)

iml = pyautogui.screenshot(region=(400, 400, 1200, 175))
iml.save(r"C:\Users\noela\Documents\human benchmark\typer.png")
img = cv2.imread('typer.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Result', img)
cv2.waitKey(1)
word = pytesseract.image_to_string(img).replace('\n', ' ')
if word.startswith('['):
    word = word[1:]
print(word)
pyautogui.typewrite(word)
#for x in word:
#    pyautogui.press(x)