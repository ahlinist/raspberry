from gpiozero import Robot
from .two_wheel_chassis import TwoWheelChassis


class ChassisFactory:
    @staticmethod
    def get_two_wheel_chassis(in1, in2, in3, in4):
        TwoWheelChassis(Robot(left=(in1, in2), right=(in3, in4)))
