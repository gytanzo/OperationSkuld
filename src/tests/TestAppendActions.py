import unittest
import BackEnd.key
import time

time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        BackEnd.key.set_username("Zhihao")
        BackEnd.key.send_key("a")
        BackEnd.key.append_actions()
        with open("Actions.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Zhihao inputted command "a"')
        BackEnd.key.set_username("Taco")
        BackEnd.key.send_key("START")
        BackEnd.key.append_actions()
        with open("Actions.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] Taco inputted command "START"')


if __name__ == '__main__':
    unittest.main()
