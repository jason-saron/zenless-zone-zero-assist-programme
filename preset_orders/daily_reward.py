import time
import win32gui, win32con
import pyautogui
from pynput.keyboard import Controller, Key
from coordinate_records.resolution_1920_1080 import coordinate
from utils.simplify_pyautogui_interface import cursor_moveTo, cursor_click

keyboard = Controller()


def daily_reward_orders():
	# 获得绝区零游戏窗口句柄，激活窗口
	hwnd = win32gui.FindWindow(None, "绝区零")
	win32gui.SetForegroundWindow(hwnd)  # 让游戏窗口获得焦点
	# 等待游戏加载资源
	time.sleep(3)
	pyautogui.click(x=960, y=540)
	# 确保进入游戏
	time.sleep(12)

	# 完成咖啡日常的自动化操作
	complete_coffee()
	# 完成录像店经营的自动化操作
	complete_store_operation()
	# 完成每日奖励获取的自动化操作
	harvest_daily_reward()
	# 在完成后自动关闭游戏，以及启动器
	shut_down()

def open_quick_menu():
	# 打开快捷菜单
	keyboard.press(Key.f2)
	print("已打开快捷菜单")
	time.sleep(1)
	keyboard.release(Key.f2)
	print("已经释放 f2 按键")
	time.sleep(2)

def click_daily_tag():
	# 首先点击 日常 标签按钮
	pyautogui.click(x=coordinate['daily_tag'][0], y=coordinate['daily_tag'][1])
	print("已点击 日常 标签按钮")
	time.sleep(2)

def complete_coffee():
	open_quick_menu()
	click_daily_tag()

	# 将光标移动到指定位置
	pyautogui.moveTo(x=coordinate['drag_press_point'][0], y=coordinate['drag_press_point'][1])
	time.sleep(1)
	# 进行选项卡拖动
	pyautogui.dragTo(x=coordinate['drag_release_point'][0], y=coordinate['drag_release_point'][1], duration=2, button='left')
	print('完成选项卡拖动')
	time.sleep(1)
	pyautogui.moveTo(x=coordinate['coffee_btn_after_first_drag'][0], y=coordinate['coffee_btn_after_first_drag'][1])
	print('光标已移动到咖啡选项处')
	time.sleep(1)
	pyautogui.click(x=coordinate['coffee_btn_after_first_drag'][0], y=coordinate['coffee_btn_after_first_drag'][1])
	print('已点击咖啡选项')
	time.sleep(2)
	cursor_click(coordinate, 'portal_confirm_btn')
	print('已点击确认按钮')
	time.sleep(5)

	# 靠近咖啡师
	keyboard.press('w')
	time.sleep(1)
	keyboard.release('w')

	# 进行交互
	keyboard.press('f')
	time.sleep(2)
	keyboard.release('f')
	# 获取咖啡
	cursor_moveTo(coordinate, 'get_coffee_btn')
	time.sleep(1)
	cursor_click(coordinate, 'get_coffee_btn')
	time.sleep(2)
	# 确认获取咖啡
	cursor_moveTo(coordinate, 'item_confirm_btn')
	cursor_click(coordinate, 'item_confirm_btn')
	time.sleep(1)

	print("完成咖啡日常")


def complete_store_operation():
	open_quick_menu()
	click_daily_tag()

	# 将光标移动到指定位置
	pyautogui.moveTo(x=coordinate['drag_press_point'][0], y=coordinate['drag_press_point'][1])
	time.sleep(1)
	# 进行选项卡拖动
	pyautogui.dragTo(x=coordinate['drag_release_point'][0], y=coordinate['drag_release_point'][1], duration=2, button='left')
	print('完成选项卡拖动')
	time.sleep(1)

	# 点击 录像店经营 传送
	cursor_click(coordinate, 'store_operation_btn_after_second_drag')
	time.sleep(1)
	cursor_click(coordinate, 'portal_confirm_btn')

	# 等待数据加载
	time.sleep(4)

	# 交互
	keyboard.press('f')
	time.sleep(1)
	keyboard.release('f')
	time.sleep(1)
	cursor_moveTo(coordinate, 'check_operation_btn')
	time.sleep(1)
	cursor_click(coordinate, 'check_operation_btn')
	print('完成交互，进入经营界面')

	# 确认经营结果
	time.sleep(2)
	cursor_click(coordinate, 'cancel_note_btn')
	# 选择宣传人
	time.sleep(2)
	cursor_click(coordinate, 'select_employee')
	print("进入宣传人选择界面")
	time.sleep(1)
	cursor_click(coordinate, 'confirm_employee')
	print("完成宣传人选择")
	# 选择影片
	time.sleep(2)
	cursor_click(coordinate, 'select_commodity')
	print("进入影片选择界面")
	time.sleep(1)
	cursor_click(coordinate, 'auto_select_commodity')
	print("影片选择完成")
	# 完成经营，确认结束
	time.sleep(2)
	cursor_click(coordinate, 'start_store_operation')
	print("已点击开始经营按钮")
	time.sleep(2)
	cursor_click(coordinate, 'start_operation_confirm_btn')
	print("已确认开始经营")
	time.sleep(2)
	cursor_click(coordinate, 'final_operation_confirm_btn')
	cursor_click(coordinate, 'final_operation_confirm_btn')
	print("录像店经营日常完成")
	time.sleep(3)

def harvest_daily_reward():
	open_quick_menu()

	cursor_click(coordinate, 'reward_tag', 1)
	cursor_click(coordinate, 'reward_confirm', 3)

	print("完成每日奖励领取")

def shut_down():
	hwnd = win32gui.FindWindow(None, "绝区零")
	if hwnd:
		# 发送关闭消息
		win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
		print("已发送关闭指令给游戏窗口")
	else:
		print("未找到游戏窗口")

	time.sleep(3)
	hwnd = win32gui.FindWindow(None, "米哈游启动器")
	if hwnd:
		# 发送关闭消息
		win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
		print("已发送关闭指令给启动器窗口")
	else:
		print("未找到游戏窗口")