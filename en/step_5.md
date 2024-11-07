## Simple line follower

**Note:** In this example, the motor controller board is connected so that the left motor is on pins **GPIO 7** and **GPIO 8**, and the right motor is on pins **GPIO 9** and **GPIO 10**. The left line sensor is on pin **GPIO 17**, and the right line sensor is on pin **GPIO 27**.

--- task ---

Open up **Thonny** from the Raspberry Pi **Programming** menu, and begin by setting up your motor controller board and your sensors using `gpiozero`:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from gpiozero import Robot, LineSensor
from time import sleep
from signal import pause

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

--- /code ---


--- /task ---

Underneath, write a simple line following program to test your robot.

--- task ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 9-14
---
from gpiozero import Robot, LineSensor
from time import sleep
from signal import pause

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

left_sensor.when_line = robot.left
right_sensor.when_line = robot.right
left_sensor.when_no_line = robot.forward
right_sensor.when_no_line = robot.forward
                 
pause()

--- /code ---


Don't worry if your robot tracks off its line. Just check it attempts to stay on the line.

![final](images/final.gif)
