import unittest
import Website.ChatUpdateBackEnd
import time

time = '[%s]' % (time.strftime('%H:%M:%S', time.gmtime()))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Website.ChatUpdateBackEnd.pp("gytanzo", "Hey guys"), time + " " + "[MESSAGE] gytanzo: Hey guys")
        self.assertEqual(Website.ChatUpdateBackEnd.pp("gytanzo", "down"), time + " " + '[COMMAND] gytanzo inputted command "down"')


if __name__ == '__main__':
    unittest.main()
