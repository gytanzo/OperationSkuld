import win32api
import win32con
import time

keyDelay = .01
keymap = {
    "Up": win32con.VK_UP,
    "up": win32con.VK_UP,
    "Left": win32con.VK_LEFT,
    "left": win32con.VK_LEFT,
    "Down": win32con.VK_DOWN,
    "down": win32con.VK_DOWN,
    "Right": win32con.VK_RIGHT,
    "right": win32con.VK_RIGHT,
    "b": ord("B"),
    "B": ord("B"),
    "a": ord("A"),
    "A": ord("A"),
    "y": ord("Y"),
    "Y": ord("Y"),
    "x": ord("X"),
    "X": ord("X"),
    "l": ord("L"),
    "L": ord("L"),
    "r": ord("R"),
    "R": ord("R"),
    "start": ord("S"),
    "START": ord("S"),
    "Start": ord("S"),
    "select": ord("E"),
    "SELECT": ord("E"),
    "Select": ord("E"),
}


def send_key(button):
    win32api.keybd_event(keymap[button], 0, 0, 0)
    time.sleep(keyDelay)
    win32api.keybd_event(keymap[button], 0, win32con.KEYEVENTF_KEYUP, 0)