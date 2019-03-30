import unittest
import Website.BackEnd_key
import win32ui
import sys
import json

json_up = json.dumps("Up")
json_down = json.dumps("Down")
json_left = json.dumps("Left")
json_right = json.dumps("Right")
json_start = json.dumps("Start")
json_a = json.dumps("a")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Website.BackEnd_key.set_username("PLACEHOLDER")
        self.assertEqual(Website.BackEnd_key.send_key(json_up), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_up), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_down), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_down), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_left), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_right), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_left), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_right), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_start), None)
        self.assertEqual(Website.BackEnd_key.send_key(json_a), None)


if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    win.SetbForegroundWindow()
    win.SetFocus()
    Website.BackEnd_key.send_key(sys.argv[2])
