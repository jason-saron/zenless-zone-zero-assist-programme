import ctypes, sys

def check_is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
    sys.exit()
