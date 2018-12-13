# encoding: GBK
import sys
import time
import win32gui
import win32con


def t1():
    wndclass = None
    wndtitle = "[python] - PyCharm"
    wnd = win32gui.FindWindow(wndclass, wndtitle)
    if wnd == 0:
        print "not found"
        sys.exit(1)

    print wnd
    win32gui.CloseWindow(wnd)


def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        name = win32gui.GetWindowText(hwnd)
        print name
        if "PyCharm" in name:
            win32gui.CloseWindow(hwnd)


def t2():
    win32gui.EnumWindows(handle_window, None)
    # time.sleep(5)
    # TODO If app didn't close, force close.


if __name__ == '__main__':
    t2()
