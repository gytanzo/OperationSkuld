import win32api
import win32con
import win32ui
import time,sys

keyDelay = .1
keymap = {
    "Up": win32con.VK_UP,
    "Left": win32con.VK_LEFT,
    "Down": win32con.VK_DOWN,
    "Right": win32con.VK_RIGHT,
    "b": ord("B"),
    "a": ord("A"),
    "s": ord("S"), #start
    "e": ord("E") #select
}


def send_key(button):
    win32api.keybd_event(keymap[button], 0, 0, 0)
    time.sleep(keyDelay)
    win32api.keybd_event(keymap[button], 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    win.SetForegroundWindow()
    win.SetFocus()
    send_key(sys.argv[2])
