import time

import pyautogui
import win32gui

from coordinate_records.resolution_1920_1080 import coordinate
from permission_acquisition.PrivilegeManager import run_as_admin, check_is_admin
from utils.simplify_pyautogui_interface import cursor_moveTo

if __name__ == '__main__':
	if check_is_admin():
		print("已经以管理员身份运行")
	else:
		print("未以管理员身份运行")
		run_as_admin()
	time.sleep(2)

	try:
		hwnd = win32gui.FindWindow(None, "绝区零")
		if hwnd == 0:
			print("错误：未找到游戏窗口")
			exit(1)

		print(f"找到窗口句柄: {hwnd}")
		win32gui.SetForegroundWindow(hwnd)
		time.sleep(1)

		for _ in range(2):
			print(f"移动到坐标: {coordinate['drag_press_point']}")
			pyautogui.moveTo(x=coordinate['drag_press_point'][0], y=coordinate['drag_press_point'][1])
			time.sleep(1)

			# 进行选项卡拖动
			pyautogui.dragTo(x=coordinate['drag_release_point'][0], y=coordinate['drag_release_point'][1], duration=1,
							 button='left')
			print('完成选项卡拖动')

	except Exception as e:
		print(f"发生错误: {str(e)}")