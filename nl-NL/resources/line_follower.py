from gpiozero import Robot, LineSensor
from signal import pause

robot = Robot(left=(7, 8), right=(9, 10)) 
linker_sensor = LineSensor(17)
rechter_sensor= LineSensor(27)

linker_sensor.when_line = robot.left
rechter_sensor.when_line = robot.right
linker_sensor.when_no_line = robot.forward
rechter_sensor.when_no_line = robot.forward
                 
pause()
