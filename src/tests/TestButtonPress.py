import unittest
import BackEnd.ButtonPress
import win32ui
import sys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(BackEnd.ButtonPress.send_key("Down"), None)
        self.assertEqual(BackEnd.ButtonPress.send_key("Down"), None)
        self.assertEqual(BackEnd.ButtonPress.send_key("Down"), None)
        self.assertEqual(BackEnd.ButtonPress.send_key("Down"), None)


if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    win.SetbForegroundWindow()
    win.SetFocus()
    BackEnd.ButtonPress.send_key(sys.argv[2])
