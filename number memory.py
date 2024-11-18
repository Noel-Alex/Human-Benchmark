import pyautogui
import pytesseract
import cv2
import win32api, win32con
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\noela\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

words = []

time.sleep(5)

while True:
    time.sleep(1)
    iml = pyautogui.screenshot(region=(600, 375, 800, 100))
    iml.save(r"C:\Users\noela\Documents\human benchmark\number.png")
    img = cv2.imread('number.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('Result', img)
    cv2.waitKey(1)
    word = pytesseract.image_to_string(img)
    time.sleep(4)
    pyautogui.typewrite(word)

