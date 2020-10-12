## Het laatste algoritme

Nu je waarden uitvoert die de motoren kunnen gebruiken, is het tijd om deze waarden in te voeren.

Om te beginnen ga je de `while True` lus veranderen in een **generator**. Een generator lijkt een beetje op een functie, behalve dat deze continu zal draaien en alleen waarden `oplevert` wanneer er om wordt gevraagd.

\--- task \---

Maak op deze manier van je lus een generator:

```python
def motor_snelheid():
    while True:
        links_detectie  = int(linker_sensor.value)
        rechts_detectie = int(rechter_sensor.value)
        ## Fase 1
        if links_detectie  == 0 and rechts_detectie == 0:
            linker_motor = 1
            rechter_motor = 1
        ## Fase 2
        if links_detectie  == 0 and rechts_detectie == 1:
            linker_motor = -1
        if links_detectie  == 1 and rechts_detectie == 0:
            rechter_motor = -1
        #print(rechter_motor, linker_motor)
        yield (rechter_motor, linker_motor)
```

\--- /task \---

Nu hoef je alleen maar te zeggen dat de `bron` van de motorwaarden van de robot het resultaat zal zijn van de generator.

\--- task \---

Voeg deze regel code onder de generator toe:

```python
robot.source = motor_snelheid()
```

\--- /task \---

Om ervoor te zorgen dat de robot niet eeuwig blijft draaien, en om alle componentverbindingen netjes te sluiten, kun je optioneel ook de volgende regels toevoegen:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
linker_sensor.close()
rechter_sensor.close()
```

\--- task \---

Voer nu je code uit en test je robot over een baan.

\--- /task \---

Soms werkt de robot een beetje te snel, zodat je de code een beetje kunt aanpassen zoals in het volgende voltooide script wordt weergegeven. Dit voegt een snelheidsvermenigvuldiger toe om de robot een beetje te vertragen.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
linker_sensor = LineSensor(17)
rechter_sensor = LineSensor(27)

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
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> Je browser ondersteunt geen WebM-video, dus probeer Firefox of Chrome. </video>