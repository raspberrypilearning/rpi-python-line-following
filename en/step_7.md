## The final follower

Your code prints the values the motors can use. 

--- task ---

Change your `while True` loop into a **generator**. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8-22
---
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        # Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        # Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        # print(r, l)
        yield (right_mot, left_mot)

--- /code ---

A generator is like a function, but it runs continually and will only `yield` values when it is asked for them.

--- /task ---

Now all you need to do is to say that the `source` of the robot's motor values is going to be the result of the generator.

--- task ---

Add in this line of code below the generator:

```python
robot.source = motor_speed()
```

--- /task ---

To make sure that the robot doesn't keep running forever, and to close all the components' connections cleanly, you can optionally add these lines to the end of your code:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

--- task ---

Now run your code and test your robot over a track.

--- /task ---

Sometimes the robot runs too fast. 

--- task ---

Add a speed multiplier to slow the robot down.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8, 24
---
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
        # Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        # Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        # print(r, l)
        yield (right_mot * speed, left_mot * speed)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()

--- /code ---

--- /task ---