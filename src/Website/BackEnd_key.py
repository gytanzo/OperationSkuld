import win32api
import win32con
import time
import Website.BackEnd_ChatUpdate
import json

keyDelay = .01
keymap = {
    "WINDOWS": win32con.VK_LWIN,
    "UP": win32con.VK_UP,
    "LEFT": win32con.VK_LEFT,
    "DOWN": win32con.VK_DOWN,
    "RIGHT": win32con.VK_RIGHT,
    "B": ord("B"),
    "A": ord("A"),
    "Y": ord("Y"),
    "X": ord("X"),
    "L": ord("L"),
    "R": ord("R"),
    "START": ord("S"),
    "SELECT": ord("E"),
}


def set_username(string):
    global username
    username = string


listOfActions = []


set_username("kappa")


def send_key(json_input):
    key_input = json.loads(json_input)
    if key_input in ['WINDOWS', 'UP', 'DOWN', 'LEFT', 'RIGHT', 'START', 'SELECT', 'X', 'Y', 'A', 'B', 'l', 'R']:
        win32api.keybd_event(keymap[key_input], 0, 0, 0)
        time.sleep(keyDelay)
        win32api.keybd_event(keymap[key_input], 0, win32con.KEYEVENTF_KEYUP, 0)
        message = Website.BackEnd_ChatUpdate.pp(username, key_input)
        listOfActions.append(message)
    else:
        message = Website.BackEnd_ChatUpdate.pp(username, key_input)
        listOfActions.append(message)
    return


def append_actions():
    contents = listOfActions
    with open("chat.txt", 'a') as f:
        for item in contents:
            f.write(item+'\n')
