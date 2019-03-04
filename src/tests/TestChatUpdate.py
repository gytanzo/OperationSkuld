import unittest
import Website.BackEnd_ChatUpdate
import time

time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Website.BackEnd_ChatUpdate.pp("gytanzo", "Hey guys"), time + " " + "[MESSAGE] gytanzo: Hey guys")
        self.assertEqual(Website.BackEnd_ChatUpdate.pp("gytanzo", "down"), time + " " + '[COMMAND] gytanzo inputted command "down"')


if __name__ == '__main__':
    unittest.main()
