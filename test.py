import pyautogui
import pytesseract
import cv2
import win32api, win32con
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\noela\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

time.sleep(5)

iml = pyautogui.screenshot(region=(400, 400, 1200, 175))
iml.save(r"C:\Users\noela\Documents\human benchmark\typer.png")
