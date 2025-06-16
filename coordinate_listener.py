from pynput import mouse
from permission_acquisition.PrivilegeManager import run_as_admin

def on_click(x, y, button, pressed):
    if pressed:  # 监听按下事件
        print(f"鼠标点击坐标: ({x}, {y}) - 按键: {button}")

run_as_admin()

# 创建监听器
listener = mouse.Listener(on_click=on_click)
listener.start()

# 保持监听循环
listener.join()
