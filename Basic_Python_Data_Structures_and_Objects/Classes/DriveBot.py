#Create a python class called DriveBot. Within this class, create instance variables for motor_speed, sensor_range, and direction. All of these should be initialized to 0 by default. After setting up the class, create an object from the class called robot_1. Set the motor_speed to 5, the direction to 90, and the sensor_range to 10. Use the provided print statements to check your work!

# Define the DriveBot class here!
class DriveBot:
  def __init__(self, motor_speed=0, sensor_range=0, direction=0):
    self.motor_speed = motor_speed
    self.sensor_range = sensor_range
    self.direction = direction

robot_1 = DriveBot(motor_speed=5,sensor_range=10, direction=90)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)