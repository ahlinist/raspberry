import unittest
from unittest.mock import Mock
from src.chassis.two_wheel_chassis import TwoWheelChassis


class TestTwoWheelChassis(unittest.TestCase):

    def setUp(self):
        self.robot = Mock()
        self.chassis = TwoWheelChassis(self.robot)

    def test_move_forward(self):
        self.chassis.move_forward()
        self.robot.forward.assert_called_once_with()

    def test_stop_moving(self):
        self.chassis.stop_moving()
        self.robot.stop.assert_called_once_with()

    def test_turn_right(self):
        self.chassis.turn_right()
        self.robot.right.assert_called_once_with()

    def test_turn_left(self):
        self.chassis.turn_left()
        self.robot.left.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
