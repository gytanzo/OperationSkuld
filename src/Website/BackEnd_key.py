import win32api
import win32con
import time
import Website.BackEnd_ChatUpdate
import json

keyDelay = .01
keymap = {
    "Up": win32con.VK_UP,
    "REFRESH": win32con.VK_F5,
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


def set_username(string):
    global username
    username = string


listOfActions = []


def send_key(json_input):
    key_input = json.loads(json_input)
    if key_input in ['Up', 'Refresh', 'up', 'UP', 'Down', 'down', 'DOWN', 'left', 'Left', 'LEFT', 'Right', 'right', 'RIGHT', 'Start', 'start', 'START', 'Select', 'select', 'SELECT', 'x', 'X', 'Y', 'y', 'A', 'a', 'B', 'b', 'l', 'L', 'R', 'r']:
        win32api.keybd_event(keymap[key_input], 0, 0, 0)
        time.sleep(keyDelay)
        win32api.keybd_event(keymap[key_input], 0, win32con.KEYEVENTF_KEYUP, 0)
        message = Website.BackEnd_ChatUpdate.pp(username, key_input)
        listOfActions.append(message)
    else:
        message = Website.BackEnd_ChatUpdate.pp(username, key_input)
        listOfActions.append(message)


def append_actions():
    contents = listOfActions
    with open("chat.txt", 'a') as f:
        for item in contents:
            f.write(item+'\n')
