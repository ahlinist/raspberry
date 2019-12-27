class TwoWheelChassis:
    def __init__(self, robot):
        self.robot = robot

    def move_forward(self):
        self.robot.forward()

    def stop_moving(self):
        self.robot.stop()

    def turn_right(self):
        self.robot.right()

    def turn_left(self):
        self.robot.left()
