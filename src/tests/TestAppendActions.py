import unittest
import Website.BackEnd_key
import time
time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Website.BackEnd_key.set_username("Zhihao")
        Website.BackEnd_key.send_key("a")
        Website.BackEnd_key.append_actions()
        with open("chat.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Zhihao inputted command "a"')
        Website.BackEnd_key.set_username("Taco")
        Website.BackEnd_key.send_key("START")
        Website.BackEnd_key.append_actions()
        with open("chat.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Taco inputted command "START"')

if __name__ == '__main__':
    unittest.main()
