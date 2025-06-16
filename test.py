import win32gui


def get_all_windows():
	windows = []

	def callback(hwnd, extra):
		if win32gui.IsWindowVisible(hwnd):
			title = win32gui.GetWindowText(hwnd)
			if title:  # 只收集有标题的窗口
				windows.append({
					'hwnd': hwnd,
					'title': title,
					'rect': win32gui.GetWindowRect(hwnd)
				})
		return True

	win32gui.EnumWindows(callback, None)
	return windows


# 获取所有窗口并打印
all_windows = get_all_windows()
for i, window in enumerate(all_windows, 1):
	print(f"{i}. 句柄: {window['hwnd']}")
	print(f"   标题: {window['title']}")
	print(f"   位置: {window['rect']}\n")