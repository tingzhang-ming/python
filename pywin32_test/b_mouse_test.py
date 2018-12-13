import time
import win32api
import win32con


def t1():
    print win32api.GetCursorPos()
    win32api.SetCursorPos((1000, 100))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


if __name__ == '__main__':
    t1()
