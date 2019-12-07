import unittest
from src.state import State


class TestState(unittest.TestCase):

    def test_is_light(self):
        self.assertEqual(State().light, None, "Should be None")

    def test_is_noisy(self):
        self.assertEqual(State().noise, None, "Should be None")

    def test_motion(self):
        self.assertEqual(State().motion, 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()
