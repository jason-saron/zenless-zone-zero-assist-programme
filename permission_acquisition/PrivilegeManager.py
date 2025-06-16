import ctypes, sys

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("当前已是管理员模式！")
    else:
        print("尝试提升权限...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

run_as_admin()