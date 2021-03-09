## Programmer un algorithme de suivi de ligne

**Remarque :** Dans cet exemple, la carte du contrôleur moteur est connectée de sorte que le moteur gauche soit sur des broches **GPIO 7** et **GPIO 8**, et le moteur droit est sur des broches **GPIO 9** et **GPIO 10**. Le capteur de la ligne gauche est sur la broche **GPIO 17**, et le capteur de la ligne droite est sur la broche **GPIO 27**.

--- task ---

Ouvre **mu** depuis le menu Raspberry Pi **Programmation** et commence par configurer ta carte contrôleur de moteur et tes capteurs en utilisant `gpiozero` :

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)
```

--- /task ---

Pour commencer, écris un algorithme de suivi de ligne vraiment simple, juste pour tester que ton robot fonctionne.

Le module `gpiozero` peut appeler une fonction selon si une ligne a été détectée ou non. Par exemple :

```python
left_sensor.when_line = function_name_to_call
left_sensor.when_no_line = other_function_name_to_call
```

Cela dira au robot de faire quelque chose lorsque le `left_sensor` détecte qu'il n'est pas au-dessus d'une ligne. En disant au robot d'avancer quand aucune ligne n'a été détectée, mais de tourner si une ligne est détectée, tu peux produire un comportement de suivi de ligne très basique.

--- task ---

Ajoute quatre lignes de code à ton programme de robot pour produire un algorithme de suivi de ligne de base.

--- /task ---

--- hints ---
 --- hint ---

Les lignes doivent effectuer les tâches suivantes :

1. S'il y a une ligne sous le capteur de gauche, tourner à gauche
2. S'il y a une ligne sous le capteur droit, tourner à droite
3. S'il n'y a pas de ligne sous le capteur droit, avancer
4. S'il n'y a pas de ligne sous le capteur gauche, avancer

--- /hint --- --- hint ---

La syntaxe utilisée dans l'exemple de programme est la suivante pour la première ligne :

```python
left_sensor.when_line = robot.left
```

Maintenant, essaie de compléter les trois lignes restantes.

--- /hint --- --- hint ---

Voici les quatre lignes de code dont tu as besoin. Si tu exécutes ton code à partir du terminal, tu devras également ajouter `pause()` à la fin.

```python
left_sensor.when_line = robot.left
right_sensor.when_line = robot.right
left_sensor.when_no_line = robot.forward
right_sensor.when_no_line = robot.forward

pause()
```

--- /hint ------ /hints ---

Ne t’inquiète pas si ton robot quitte un peu sa ligne. Observe simplement s'il tente de rester sur la ligne. Voici un exemple de robot roulant sur une piste de base avec cet algorithme.

![final](images/final.gif)