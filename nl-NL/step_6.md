## Plan een beter algoritme

Het vorige algoritme is misschien in orde, het kan gemakkelijk worden verbeterd. Laten we eens kijken hoe een beter algoritme eruit zou kunnen zien!

Wanneer een lijnsensor boven een lijn is, geeft deze een `1`. Wanneer het van een lijn af is, geeft het een `0`.

De motoren werken echter iets anders: De robot stuurt de rechtermotor naar voren wanneer hij een `1` signaal naar die motor ontvangt. Wanneer het een `-1` ontvangt, stuurt het de motor achteruit.

Laten we eens kijken naar een algoritme dat rekening houdt met de positie van de robot, de status van de lijnsensoren en de acties die nodig zijn voor de motoren.

1. De robot is perfect op de lijn en zou vooruit moeten rijden:
    
    - Beide lijnsensoren zijn van de lijn en geven een `0`
    - Beide motoren moeten `1` ontvangen om vooruit te rijden

2. De robot is naar links afgeweken en moet naar rechts draaien:
    
    - De juiste sensor is op de lijn en geeft een `1`
    - De linkersensor is van de lijn en geeft een `0`
    - De linkermotor moet achteruit lopen en dus een `-1` ontvangen
    - De rechtermotor moet vooruit lopen en dus een `1` ontvangen

3. De robot is naar rechts afgeweken en moet naar links draaien:
    
    - De rechtersensor is van de lijn en geeft een `0`
    - De linkersensor is op de lijn en geeft een `1`
    - De linkermotor moet vooruit lopen en dus een `1` ontvangen
    - De rechtermotor moet achteruit lopen en dus een `-1` ontvangen

Hoe kun je dit in code laten gebeuren? Ten eerste maak je een oneindige lus om de sensorwaarden te bekijken.

--- task ---

Voeg in een nieuw bestand de volgende regels code toe en voer het uit. Vergeet niet om de pinnummers aan te passen als je verschillende GPIO-pinnen hebt gebruikt.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
linker_sensor = LineSensor(17)
rechter_sensor= LineSensor(27)

while True:
    links_detectie = int(linker_sensor.value)
    rechts_detectie = int(rechter_sensor.value)
    print(links_detectie, rechts_detectie)
```

Beweeg de robot nu heen en weer over de lijn om te zien wat er gebeurt.

--- /task ---

Hopelijk zou je de binaire output van de sensoren moeten zien.

![sensor_uitvoer](images/sensor_output.gif)

Dus nu je de sensoruitvoer hebt, moet je het een beetje veranderen voordat je het naar de motoren stuurt. Volgens het bovenstaande algoritme:

- Als beide sensoren `0` uitvoeren, moeten beide motoren `1` ontvangen
- Als de rechtersensor `1` uitvoert, moet de linkermotor `-1` ontvangen
- Als de linkersensor `1` uitvoert, moet de rechtermotor `-1` ontvangen

--- task ---

Maak binnen de `while True`-lus twee nieuwe variabelen met de naam `linker_motor` en `rechter_motor`. Deze variabelen moeten dezelfde waarde hebben die je wilt dat de motoren ontvangen. Je kunt hun waarden gewoon binnen de lus afdrukken.

--- /task ---

--- hints ---
 --- hint ---

Volgens het bovenstaande algoritme, `if links_detectie == 0 and rechts_detectie == 0:`, wat wil je dan dat de waarden van `linker_motor` en `rechter_motor` zijn?

--- /hint --- --- hint ---

Hier is de code voor de eerste voorwaarde:

    while True:
        links_detectie = int(linker_sensor.value)
        rechts_detectie = int(rechter_sensor.value)
        if links_detectie == 0 and rechts_detectie == 0:
            linker_motor = 1
            rechter_motor = 1
    

Je hebt nog twee `if` statements nodig om de sensoren te verwerken die door een lijn worden geactiveerd.

--- /hint --- --- hint ---

Hier is de voltooide code, met het print statement:

```python while True: links_detectie = int(linker_sensor.value) rechts_detectie = int(rechter_sensor.value)

    if links_detectie  == 0 and rechts_detectie == 0:
        linker_motor = 1
        rechter_motor = 1
    
    if links_detectie  == 0 and rechts_detectie == 1:
        linker_motor = -1
    if links_detectie  == 1 and rechts_detectie == 0:
        rechter_motor = -1
    
    print(right_mot, left_mot)
    

```

--- /hint ------ /hints ---

--- task ---

Wanneer je klaar bent, voer je code uit en test je hoe het werkt wanneer je de robot over de lijn beweegt.

![sensor_output2.gif](images/sensor_output2.gif)

--- /task ---