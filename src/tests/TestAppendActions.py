import unittest
import Website.keyBackEnd
import time

time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        Website.keyBackEnd.set_username("Zhihao")
        Website.keyBackEnd.send_key("a")
        Website.keyBackEnd.append_actions()
        with open("chat.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Zhihao inputted command "a"')
        Website.keyBackEnd.set_username("Taco")
        Website.keyBackEnd.send_key("START")
        Website.keyBackEnd.append_actions()
        with open("chat.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Taco inputted command "START"')


if __name__ == '__main__':
    unittest.main()
