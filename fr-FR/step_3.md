## Connecter les capteurs de ligne

Chaque capteur de ligne a trois broches : **VCC** pour l'alimentation, **GND** pour la masse et **DO** pour la sortie numérique.

![capteur de ligne](images/sensor.jpg)

--- task ---

Prends l'un de tes fils de cavalier à trois fils soudés ensemble et connecte deux de ses extrémités à la **VCC** sur chacun des deux capteurs.

![alimentation](images/power.jpg)

--- /task ---

--- task ---

Prends le deuxième de tes fils de cavalier soudés et connecte deux extrémités à la **GND** de chaque capteur de ligne.

![masse](images/ground.jpg)

--- /task ---

--- task ---

Prends tes deux fils de cavalier simples restants et connecte chacun à la **DO** sur chaque capteur de ligne.

![sortie numérique](images/digital_out.jpg)

--- /task ---

--- task ---

Maintenant, connecte les broches **VCC** des deux capteurs de ligne à une broche **5V** sur ton Raspberry Pi, et les broches **GND** des capteurs à une broche **GND** sur ton Raspberry Pi. Chacune des deux broches **DO** peut être connectée à n'importe quelle broche GPIO numérotée. Dans cet exemple, les broches **GPIO 17** et **GPIO 27** sont utilisées.

![connecté](images/connected.jpg)

--- /task ---