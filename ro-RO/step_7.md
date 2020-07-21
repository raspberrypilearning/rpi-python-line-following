## Algoritmul final

Acum că afișezi valorile pe care motoarele le pot utiliza, este momentul să le transmiți.

Pentru inceput, vei transforma o buclă `while True` în **generator**. Un generator se asemănă cu o funcție, cu excepția faptului că funcționează în mod continuu și furnizează valori `yield` când cineva le cere.

\--- task \---

Turn your loop into a generator like this:

```python
def viteza_motor():
    while True:
        detectare_stanga = int(senzor_stanga.value)
        detectare_dreapta = int(senzor_dreapta.value)
        ## Stage 1
        if detectare_stanga == 0 and detectare_dreapta == 0:
            motor_stanga= 1
            motor_dreapta = 1
        ## Stage 2
        if detectare_stanga == 0 and detectare_dreapta == 1:
            motor_stanga= -1
        if detectare_stanga == 1 and detectare_dreapta == 0:
            motor_dreapta = -1
        #print(r, l)
        yield (motor_dreapta, motor_stanga)
```

\--- /task \---

Now all you need to do is to say that the `source` of the robot's motor values is going to be the result of the generator.

\--- task \---

Add in this line of code below the generator:

```python
robot.source = viteza_motor()
```

\--- /task \---

To make sure that the robot doesn't keep running forever, and to close all the components connections cleanly, you can optionally add in these lines as well:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
senzor_stanga.close()
senzor_dreapta.close()
```

\--- task \---

Now run your code and test your robot over a track.

\--- /task \---

Sometimes the robot runs a little too fast, so you can tweak your code a bit as shown in the following completed script. This adds in a speed multiplier to slow the robot down a little.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))
senzor_stanga = LineSensor(17)
senzor_dreapta = LineSensor(27)

viteza = 0.65

def viteza_motor():
    while True:
       detectare_stanga = int(senzor_stanga.value)
       detectare_dreapta = int(senzor_dreapta.value)
       ## Stage 1
       if detectare_stanga == 0 and detectare_dreapta == 0:
           motor_stanga = 1
           motor_dreapta= 1
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
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> Browserul tău nu suportă video de tip WebM, prin urmare încearcă FireFox sau Chrome. </video>