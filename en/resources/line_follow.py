from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)


def motor_speed():
    while True:
        l = int(left_sensor.value)
        r = int(right_sensor.value)
        ## Stage 1
        if l == 0 and r == 0:
            l = 1
            r = 1
        ## Stage 2
        if l == 0 and r == 1:
            l = -1
        if l == 1 and r == 0:
            r = -1
        #print(r, l)
        yield (r * 0.65, l * 0.65)

robot.source = motor_speed()
#print("hi")
# #motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
