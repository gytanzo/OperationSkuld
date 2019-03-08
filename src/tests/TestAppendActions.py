import unittest
import Website.BackEnd_key
import time
time = '[%s]' % (time.strftime('%H:%M:%S', time.localtime()))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Website.BackEnd_key.set_username("Gytanzo")
        Website.BackEnd_key.send_key("Start")
        Website.BackEnd_key.set_username("Meep")
        Website.BackEnd_key.send_key("Down")
        Website.BackEnd_key.set_username("ChitogeSucks")
        Website.BackEnd_key.send_key("Down")
        Website.BackEnd_key.set_username("Xenhe")
        Website.BackEnd_key.send_key("A")
        Website.BackEnd_key.set_username("GrainsOfRice")
        Website.BackEnd_key.send_key("Down")
        Website.BackEnd_key.set_username("GravityPanda")
        Website.BackEnd_key.send_key("A")
        Website.BackEnd_key.set_username("VentusAir")
        Website.BackEnd_key.send_key("B")
        Website.BackEnd_key.append_actions()
        with open("chat.txt") as f:
            string = ""
            for line in f:
                string = line.rstrip()
            self.assertEqual(string, time + " " + '[COMMAND] VentusAir inputted command "B"')


if __name__ == '__main__':
    unittest.main()
