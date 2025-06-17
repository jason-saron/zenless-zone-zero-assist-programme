import time
import tkinter as tk
from tkinter import scrolledtext
import win32con
import win32gui

from permission_acquisition.PrivilegeManager import run_as_admin, check_is_admin
from preset_orders.daily_reward import daily_reward_orders


class AppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("米哈游自动助手")
        self.root.geometry("500x600")

        # 将日志区域放在Frame中并限制其高度
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill='both')

        self.log_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
        self.log_area.pack(expand=True, fill='both')

        # 将按钮放在单独的Frame中
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='x', pady=10)

        self.start_button = tk.Button(button_frame, text="开始执行", command=self.start_process)
        self.start_button.pack()

    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def start_process(self):
        self.start_button.config(state='disabled')
        self.log_message("正在获取管理员权限...")
        run_as_admin()

        while True:
            if check_is_admin():
                self.log_message("已获取管理员权限！")
                break
            else:
                self.log_message("获取管理员权限失败！尝试重新获取...")
                run_as_admin()

        hwnd = win32gui.FindWindow(None, "米哈游启动器")
        if hwnd:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            self.log_message("已发送关闭指令给启动器窗口")
        else:
            self.log_message("未找到启动器窗口，开始领取奖励...")
            daily_reward_orders(AppGUI)
            self.log_message("每日奖励领取完成！")

        self.start_button.config(state='normal')


if __name__ == '__main__':
    app = AppGUI()
    app.root.mainloop()