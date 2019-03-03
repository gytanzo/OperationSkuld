import unittest
import BackEnd.ChatUpdate
import time

time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(BackEnd.ChatUpdate.pp("gytanzo", "Hey guys"), time + " " + "[MESSAGE] gytanzo: Hey guys")
        self.assertEqual(BackEnd.ChatUpdate.pp("gytanzo", "down"), time + " " + '[COMMAND] gytanzo inputted command "down"')


if __name__ == '__main__':
    unittest.main()
