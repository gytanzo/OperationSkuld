import unittest
import Website.keyBackEnd
import win32ui
import sys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Website.keyBackEnd.send_key("Up"), None)
        self.assertEqual(Website.keyBackEnd.send_key("up"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Down"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Down"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Left"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Right"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Left"), None)
        self.assertEqual(Website.keyBackEnd.send_key("Right"), None)
        self.assertEqual(Website.keyBackEnd.send_key("start"), None)
        self.assertEqual(Website.keyBackEnd.send_key("a"), None)


if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    win.SetbForegroundWindow()
    win.SetFocus()
    Website.keyBackEnd.send_key(sys.argv[2])
