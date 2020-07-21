## Programarea unui algoritm de urmărire a liniei

**Notă:** În acest exemplu, placa de comandă a motorului este conectată astfel încât motorul din stânga să fie pe pinii **GPIO 7** și **GPIO 8**, iar motorul din dreapta să fie în pinii **GPIO 9** și **GPIO 10**. Senzorul de urmărire a liniei din stânga se află pe pinul **GPIO 17**, iar senzorul de urmărire a liniei din dreapta este pe pinul **GPIO 27**.

\--- task \---

Open up **mu** from the Raspberry Pi **Programming** menu, and begin by setting up your motor controller board and your sensors using `gpiozero`:

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
senzor_stanga = LineSensor(17)
senzor_dreapta = LineSensor(27)
```

\--- /task \---

To begin with, write a really simple line following algorithm, just to test that your robot is working.

The `gpiozero` module can call a function depending on whether or not a line has been detected. For example:

```python
senzor_stanga.when_line = numele_funcției_de_apelat
senzor_stanga.when_no_line = numele_celeilalte_funcții_de_apelat
```

This will tell the robot to do something when the `left_sensor` detects that it is not above a line. By telling the robot to go forward when no line has been detected, but to turn if a line is detected, you can produce very basic line following behavior.

\--- task \---

Add four lines of code to your robot program to produce a basic line following algorithm.

\--- /task \---

\--- hints \--- \--- hint \---

The lines should perform the following tasks:

1. Dacă există o linie sub senzorul din stânga, virează la stânga
2. Dacă există o linie sub senzorul din dreapta, virează la dreapta
3. Dacă nu există linie sub senzorul din dreapta, mergi înainte
4. If there's no line under the left sensor, drive forwards

\--- /hint \--- \--- hint \---

The syntax used in the example program is as follows for the first line:

```python
senzor_stanga.when_line = robot.left
```

Now try to complete the remaining three lines.

\--- /hint \--- \--- hint \---

Here are the four lines of code you need. If you're running your code from the terminal, you'll need to add `pause()` at the end as well.

```python
senzor_stanga.when_line = robot.left
senzor_dreapta.when_line = robot.right
senzor_stanga.when_no_line = robot.forward
senzor_dreapta.when_no_line = robot.forward

pause()
```

\--- /hint \--- \--- /hints \---

Don't worry if you're robot tracks off its line a bit. Just observe if it attempts to stay on the line. Here's an example of a robot running on a basic track with this algorithm.

![final](images/final.gif)