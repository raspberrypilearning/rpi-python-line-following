from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
senzor_stanga = LineSensor(17)
senzor_dreapta= LineSensor(27)

viteza = 0.65

def viteza_motor():
    while True:
        detectare_stanga  = int(senzor_stanga.value)
        detectare_dreapta = int(senzor_dreapta.value)
        ## Stage 1
        if detectare_stanga == 0 and detectare_dreapta == 0:
            motor_stanga = 1
            motor_dreapta = 1
        ## Stage 2
        if detectare_stanga == 0 and detectare_dreapta == 1:
            motor_stanga = -1
        if detectare_stanga == 1 and detectare_dreapta == 0:
            motor_dreapta = -1
        #print(r, l)
        yield (motor_dreapta * viteza, motor_stanga * viteza)

robot.source = viteza_motor()

sleep(60)
robot.stop()
robot.source = None
robot.close()
senzor_stanga.close()
senzor_dreapta.close()
