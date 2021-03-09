## Élaborer un meilleur algorithme

L'algorithme précédent peut être correct, il peut facilement être amélioré. Voyons à quoi pourrait ressembler un meilleur algorithme !

Lorsqu'un capteur de ligne est au-dessus d'une ligne, il donne un `1`. Quand il est hors ligne, il donne un `0`.

Les moteurs fonctionnent cependant légèrement différemment : le robot, chaque fois qu'il reçoit un signal `1` au bon moteur, fait avancer ce moteur. Lorsqu'il reçoit un `-1`, il fait reculer le moteur.

Jetons un coup d'œil à un algorithme qui prend en compte la position du robot, les états des capteurs de lignes et les actions requises des moteurs.

1. Le robot est parfaitement en ligne et devrait avancer :
    
    - Les deux capteurs de ligne sont hors ligne et donnent un `0`
    - Les deux moteurs doivent recevoir `1` pour avancer

2. Le robot a dérivé à gauche et a besoin de tourner à droite :
    
    - Le capteur droit est sur la ligne et donne un `1`
    - Le capteur de gauche est hors ligne et donne un `0`
    - Le moteur gauche devrait tourner en arrière et recevoir donc un `-1`
    - Le moteur droit doit tourner vers l'avant et recevoir ainsi un `1`

3. Le robot a dérivé à droite et a besoin de tourner à gauche :
    
    - Le capteur droit est hors ligne et donne un `0`
    - Le capteur gauche est sur la ligne et donne un `1`
    - Le moteur gauche devrait tourner vers l'avant et donc recevoir un `1`
    - Le moteur droit doit s'exécuter en arrière et recevoir donc un `-1`

Comment peux-tu faire en sorte que cela se fasse dans le code ? Tout d'abord, tu vas créer une boucle infinie pour voir les valeurs du capteur.

--- task ---

Dans un nouveau fichier, ajoute les lignes de code suivantes et exécute-le. N'oublie pas d'ajuster les numéros de broches si tu as utilisé des broches GPIO différentes.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

while True:
    left_detect  = int(left_sensor.value)
    right_detect = int(right_sensor.value)
    print(left_detect, right_detect)
```

Maintenant, déplace le robot d'avant en arrière sur la ligne pour voir ce qui se passe.

--- /task ---

Espérons que tu devrais voir la sortie binaire des capteurs.

![sensor_output](images/sensor_output.gif)

Alors maintenant que tu as la sortie du capteur, tu devras la modifier un peu avant de l'envoyer aux moteurs. Selon l'algorithme ci-dessus :

- Si les deux capteurs sortent `0`, alors les deux moteurs devraient recevoir `1`
- Si le capteur de droite donne `1`, alors le moteur de gauche devrait recevoir `-1`
- Si le capteur gauche donne `1`, alors le moteur droit devrait recevoir `-1`

--- task ---

À l'intérieur de la boucle `while True` , crée deux nouvelles variables appelées `left_mot` et `right_mot`. Ces variables doivent avoir la même valeur que celle que tu veux que les moteurs reçoivent. Tu peux simplement imprimer leurs valeurs dans la boucle.

--- /task ---

--- hints ---
 --- hint ---

Selon l'algorithme ci-dessus, `if left_detect == 0 and right_detect == 0:`, que veux-tu que les valeurs de `left_mot` et `right_mot` soient ?

--- /hint --- --- hint ---

Voici le code de la première condition :

    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
    

Tu as besoin de deux autres `if` pour gérer les capteurs déclenchés par une ligne.

--- /hint --- --- hint ---

Voici le code terminé, avec les instructions d'impression :

```python 
while True: 
    left_detect = int(left_sensor.value) 
    right_detect = int(right_sensor.value)

    if left_detect == 0 and right_detect == 0:
        left_mot = 1
        right_mot = 1
    
    if left_detect == 0 and right_detect == 1:
        left_mot = -1
    if left_detect == 1 and right_detect == 0:
        right_mot = -1
    
    print(right_mot, left_mot)
    

```

--- /hint ------ /hints ---

--- task ---

Quand tu as terminé, exécute ton code et teste comment ça marche quand tu bouges le robot sur la ligne.

![sensor_output2.gif](images/sensor_output2.gif)

--- /task ---