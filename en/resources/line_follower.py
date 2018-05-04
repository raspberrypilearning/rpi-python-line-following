from gpiozero import Robot, LineSensor
from signal import pause

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

left_sensor.when_line = robot.left
right_sensor.when_line = robot.right
left_sensor.when_no_line = robot.forward
right_sensor.when_no_line = robot.forward
                 
pause()
