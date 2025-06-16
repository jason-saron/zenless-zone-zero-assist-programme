import pyautogui
import time

def cursor_moveTo(coordinate, key, interval=1):
	pyautogui.moveTo(x=coordinate[key][0], y=coordinate[key][1])
	time.sleep(interval)

def cursor_click(coordinate, key, interval=1):
	pyautogui.click(x=coordinate[key][0], y=coordinate[key][1])
	time.sleep(interval)
