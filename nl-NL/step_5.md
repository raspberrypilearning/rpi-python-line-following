## Programmeer een lijnvolg-algoritme

**Opmerking:** in dit voorbeeld is de motorcontrollerkaart aangesloten zodat de linkermotor op de pennen **GPIO 7** en **GPIO 8** zit, en de rechtermotor op de pennen **GPIO 9** en **GPIO 10**. De linker lijnsensor bevindt zich op pen **GPIO 17**, en de rechter lijnsensor op pen **GPIO 27**.

\--- task \---

Open **mu** vanuit het Raspberry Pi **Programmeren** menu en begin met het instellen van je motorcontrollerkaart en je sensoren met `gpiozero`:

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
linker_sensor = LineSensor(17)
rechter_sensor= LineSensor(27)
```

\--- /task \---

Om te beginnen schrijf je een heel eenvoudig lijnvolg-algoritme volgt om te testen of je robot werkt.

De `gpiozero` module kan een functie aanroepen, afhankelijk van of er al dan niet een lijn is gedetecteerd. Bijvoorbeeld:

```python
linker_sensor.when_line = functienaam_om_aan_te_roepen
linker_sensor.when_no_line = andere_functienaam_om_aan_te_roepen
```

Dit vertelt de robot om iets te doen wanneer de `linker_sensor` detecteert dat deze niet boven een lijn staat. Door de robot te vertellen om vooruit te gaan wanneer er geen lijn is gedetecteerd, maar om te draaien als een lijn wordt gedetecteerd, kun je zeer basale lijnvolg-gedrag produceren.

\--- task \---

Voeg vier regels code toe aan je robotprogramma om een basis lijnvolg-algoritme te produceren.

\--- /task \---

\--- hints \--- \--- hint \---

De regels moeten de volgende taken uitvoeren:

1. Als er een lijn onder de linkersensor is, sla dan linksaf
2. Als er een lijn onder de rechtersensor is, sla dan rechtsaf
3. Als er geen lijn onder de rechtersensor is, rijd dan vooruit
4. Als er geen lijn onder de linkersensor is, rijd dan vooruit

\--- /hint \--- \--- hint \---

De syntaxis die in het voorbeeldprogramma wordt gebruikt is als volgt voor de eerste regel:

```python
linker_sensor.when_line = robot.left
```

Probeer nu de resterende drie regels te voltooien.

\--- /hint \--- \--- hint \---

Hier zijn de vier regels code die je nodig hebt. Als je de code vanaf de terminal uitvoert, moet je ook `pause()` aan het einde toevoegen.

```python
linker_sensor.when_line = robot.left
rechter_sensor.when_line = robot.right
linker_sensor.when_no_line = robot.forward
rechter_sensor.when_no_line = robot.forward

pause()
```

\--- /hint \--- \--- /hints \---

Maak je geen zorgen als je robot een beetje van zijn lijn afloopt. Kijk maar of het probeert op de lijn te blijven. Hier is een voorbeeld van een robot die met dit algoritme op een basisspoor rijdt.

![definitief](images/final.gif)