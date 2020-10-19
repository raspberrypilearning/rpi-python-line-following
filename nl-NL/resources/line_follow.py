from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
linker_sensor = LineSensor(17)
rechter_sensor= LineSensor(27)

snelheid = 0.65

def motor_snelheid():
    while True:
        links_detectie = int(linker_sensor.value)
        rechts_detectie = int(rechter_sensor.value)
        ## Fase 1
        if links_detectie == 0 and rechts_detectie == 0:
            linker_motor = 1
            rechter_motor = 1
        ## Fase 2
        if links_detectie == 0 and rechts_detectie == 1:
            linker_motor = -1
        if links_detectie == 1 and rechts_detectie == 0:
            rechter_motor = -1
        #print(rechter_motor, linker_motor)
        yield (rechter_motor * snelheid, linker_motor * snelheid)

robot.source = motor_snelheid()

sleep(60)
robot.stop()
robot.source = None
robot.close()
linker_sensor.close()
rechter_sensor.close()
