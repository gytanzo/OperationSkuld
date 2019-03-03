import unittest
import BackEnd.key


class MyTestCase(unittest.TestCase):
    def test_something(self):
        BackEnd.key.send_key("Up")
        BackEnd.key.send_key("Up")
        BackEnd.key.send_key("Down")
        BackEnd.key.send_key("Down")
        BackEnd.key.send_key("Left")
        BackEnd.key.send_key("Right")
        BackEnd.key.send_key("Left")
        BackEnd.key.send_key("Right")
        BackEnd.key.append_actions()


if __name__ == '__main__':
    unittest.main()
