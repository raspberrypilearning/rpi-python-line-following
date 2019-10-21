from gpiozero import Robot, LineSensor
from signal import pause

robot = Robot(left=(7, 8), right=(9, 10)) 
senzor_stanga = LineSensor(17)
senzor_dreapta = LineSensor(27)

senzor_stanga.when_line = robot.left
senzor_dreapta.when_line = robot.right
senzor_stanga.when_no_line = robot.forward
senzor_dreapta.when_no_line = robot.forward
                 
pause()
