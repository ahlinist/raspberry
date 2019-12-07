import unittest
from src.state import State


class TestState(unittest.TestCase):

    def test_is_dark(self):
        self.assertEqual(State.is_dark, True, "Should be True")

    def test_is_noisy(self):
        self.assertEqual(State.is_noisy, False, "Should be False")

    def test_motion(self):
        self.assertEqual(State.motion, 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()
