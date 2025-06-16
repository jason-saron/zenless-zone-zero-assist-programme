import time

import win32con
import win32gui

from permission_acquisition.PrivilegeManager import run_as_admin
from preset_orders.daily_reward import daily_reward_orders

if __name__ == '__main__':
    # 获得管理员权限
    run_as_admin()

    time.sleep(5)

    hwnd = win32gui.FindWindow(None, "米哈游启动器")
    if hwnd:
        # 发送关闭消息
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        print("已发送关闭指令给启动器窗口")
    else:
        print("未找到启动器窗口，正常进入领取奖励操作流程")

        # 执行获取每日奖励的预输入指令
        daily_reward_orders()








