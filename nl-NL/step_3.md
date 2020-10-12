## Sluit de lijnsensoren aan

Elke lijnsensor heeft drie pinnen: **VCC** voor voeding, **GND** voor aarde en **DO** voor digitale uitgang.

![lijnsensor](images/sensor.jpg)

\--- task \---

Neem een van de gesoldeerde drie-draads verbindingsdraden en verbind twee van de uiteinden met de **VCC** pin op elk van de twee sensoren.

![voeding](images/power.jpg)

\--- /task \---

\--- task \---

Neem de tweede van je gesoldeerde verbindingsdraden en verbind twee uiteinden met de **GND** pin op elke lijnsensor.

![aarde](images/ground.jpg)

\--- /task \---

\--- task \---

Neem de twee resterende verbindingsdraden en verbind ze met de **DO** pin op elke lijnsensor.

![digitale uitgang](images/digital_out.jpg)

\--- /task \---

\--- task \---

Verbind nu de **VCC** pinnen van beide lijnsensoren met een **5V** pin op je Raspberry Pi, en de **GND** pinnen van de sensoren met een **GND** pin op je Raspberry Pi. Elk van de twee **DO** pinnen kan worden aangesloten op elke genummerde GPIO pin. In dit voorbeeld worden de pinnen **GPIO 17** en **GPIO 27** gebruikt.

![verbonden](images/connected.jpg)

\--- /task \---