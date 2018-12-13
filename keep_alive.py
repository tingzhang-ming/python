import sys
import time
import win32gui
import win32api
import win32con


def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        name = win32gui.GetWindowText(hwnd)
        if "PyCharm" in name:
            win32gui.CloseWindow(hwnd)


def main():
    win32gui.EnumWindows(handle_window, None)
    win32api.SetCursorPos((1000, 100))
    while True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(10)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "exit"
        sys.exit(0)

