#Create a python class called DriveBot. Within this class, create instance variables for motor_speed, sensor_range, and direction. All of these should be initialized to 0 by default. After setting up the class, create an object from the class called robot_1. Set the motor_speed to 5, the direction to 90, and the sensor_range to 10. Use the provided print statements to check your work!

# Define the DriveBot class here!
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

      

robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(new_direction=180, new_speed=10)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

DriveBot.longitude = -50.0
DriveBot.latitude = 50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)