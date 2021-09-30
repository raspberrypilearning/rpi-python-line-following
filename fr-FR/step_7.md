## L'algorithme final

Maintenant que tu sors des valeurs que les moteurs peuvent utiliser, il est temps d'introduire ces valeurs.

Pour commencer, tu vas transformer ton `while True` en un **générateur**. Un générateur est un peu comme une fonction, sauf qu'il fonctionnera continuellement et qu'il ` donnera` des valeurs seulement quand on lui demandera.

\--- task \---

Transforme ta boucle en un générateur comme ceci :

```python
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot, left_mot)
```

\--- /task \---

Maintenant, tout ce que tu as à faire est de dire que la `source` des valeurs du moteur du robot sera le résultat du générateur.

\--- task \---

Ajoute dans cette ligne de code sous le générateur :

```python
robot.source = motor_speed()
```

\--- /task \---

Pour s'assurer que le robot ne continue pas à rouler indéfiniment, et pour fermer proprement toutes les connexions de composants, tu peux éventuellement ajouter ces lignes aussi :

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

\--- task \---

Exécute maintenant ton code et teste ton robot sur une piste.

\--- /task \---

Parfois, le robot tourne un peu trop vite, donc tu peux modifier ton code un peu comme montré dans le script terminé suivant. Cela ajoute un multiplicateur de vitesse pour ralentir un peu le robot.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

speed = 0.65

def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot * speed, left_mot * speed)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> Ton navigateur ne supporte pas la vidéo WebM, alors essaye FireFox ou Chrome. </video>