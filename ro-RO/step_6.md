## Proiectează un algoritm mai bun

Algoritmul anterior poate fi unul bun, însă poate fi îmbunătățit cu ușurință. Să vedem cum ar putea arăta un algoritm mai bun!

Atunci când un senzor este deasupra unei linii, acesta emite un `1`. Atunci când este în afara unei linii, acesta emite un `0`.

Motoarele funcționează puțin diferit însă: robotul, ori de câte ori primește un semnal `1` la motorul din dreapta, acel motor merge înainte. Când primește `-1`, motorul merge înapoi.

Să aruncăm o privire asupra unui algoritm care ia în considerare poziția robotului, stările senzorilor de urmărire a liniei și acțiunile necesare motoarelor.

1. Robotul este perfect pe linie și ar trebui să meargă înainte:
    
    - Ambii senzori de linie sunt în afara liniei și afișează valoarea `0`
    - Ambele motoare ar trebui să primească `1` pentru a merge înainte

2. Robotul s-a deplasat spre stânga și trebuie să vireze la dreapta:
    
    - Senzorul din dreapta se află pe linie și emite un `1`
    - Senzorul din stânga este în afara liniei și emite un `0`
    - Motorul din stânga trebuie să ruleze înapoi și ar trebui să primească un `-1`
    - Motorul din dreapta trebuie să ruleze înainte și ar trebui să primească un `1`

3. Robotul s-a deplasat spre dreapta și trebuie să vireze la stânga:
    
    - Senzorul din dreapta este în afara liniei și emite un `0`
    - Senzorul din stânga se află pe linie și emite un `1`
    - Motorul din stânga trebuie să ruleze înainte și ar trebui să primească un `1`
    - Motorul din dreapta ar trebui să ruleze înapoi și ar trebui să primească un `-1`

Cum poți face acest lucru în cod? Mai întâi, vei crea o buclă infinită pentru a vedea valorile senzorului.

\--- task \---

In a new file, add in the following lines of code and run it. Don't forget to adjust the pin numbers if you've used different GPIO pins.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
senzor_stanga = LineSensor(17)
senzor_dreapta = LineSensor(27)

while True:
    detectare_stanga = int(senzor_stanga.value)
    detectare_dreapta = int(senzor_dreapta.value)
    print(detectare_stanga, detectare_dreapta)
```

Now move the robot back and forth over the line to see what happens.

\--- /task \---

Hopefully, you should see the binary output from the sensors.

![sensor_output](images/sensor_output.gif)

So now that you have the sensor output, you need to alter it a little before you send it to the motors. As per the algorithm above:

- Dacă ambii senzori au ca rezultat valoarea `0`, atunci ambele motoare ar trebui să primească valoarea `1`
- Dacă rezultatul senzorului drept este `1`, atunci motorul din stânga ar trebui să primească `-1`
- Dacă rezultatul senzorul din stânga este `1`, motorul din dreapta trebuie să primească `-1`

\--- task \---

Within the `while True` loop, create two new variables called `left_mot` and `right_mot`. These variables should have the same value that you would like the motors to receive. You can simply print out their values within the loop.

\--- /task \---

\--- hints \--- \--- hint \---

According to the above algorithm, `if left_detect == 0 and right_detect == 0:`, what do you want the values of `left_mot` and `right_mot` to be?

\--- /hint \--- \--- hint \---

Here's the code for the first condition:

    while True:
        detectare_stanga = int(senzor_stanga.value)
        detectare_dreapta = int(senzor_dreapta.value)
        if detectare_stanga == 0 and detectare_dreapta == 0:
            motor_stanga = 1
            motor_dreapta = 1
    

You need two more `if` statements to handle the sensors being triggered by a line.

\--- /hint \--- \--- hint \---

Here's the completed code, with the print statements:

```python while True: left_detect = int(left_sensor.value) right_detect = int(right_sensor.value)

    if detectare_stanga == 0 and detectare_dreapta == 0:
        motor_stanga = 1
        motor_dreapta = 1
    
    if detectare_stanga == 0 and detectare_dreapta == 1:
        motor_stanga = -1
    if detectare_stanga == 1 and detectare_dreapta == 0:
        motor_dreapta = -1
    
    print(motor_dreapta, motor_stanga)
    

```

\--- /hint \--- \--- /hints \---

\--- task \---

When you are done, run your code and test how it works when you move the robot over the line.

![sensor_output2.gif](images/sensor_output2.gif)

\--- /task \---