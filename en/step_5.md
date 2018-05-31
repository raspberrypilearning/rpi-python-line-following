## Programming a line following algorithm

**Note:** In this example, the motor controller board is connected so that the left motor is on pins **GPIO 7** and **GPIO 8**, and the right motor is on pins **GPIO 9** and **GPIO 10**. The left line sensor is on pin **GPIO 17**, and the right line sensor is on pin **GPIO 27**.

--- task ---
Open up your preferred text editor or IDE on your Raspberry Pi, and begin by setting up your motor controller board and your sensors using `gpiozero`:

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)
```
--- /task ---

To begin with, write a really simple line following algorithm, just to test that your robot is working.

The `gpiozero` module can call a function depending on whether or not a line has been detected. For example:

```python
left_sensor.when_no_line = function_name_to_call
```

This will tell the robot to do something when the `left_sensor` detects that it is not above a line.
By telling the robot to go forward when no line has been detected, but to turn if a line is detected, you can produce very basic line following behavior.

--- task ---
Add four lines of code to your robot program to produce a basic line following algorithm.

--- /task ---

--- hints --- --- hint ---
The lines should perform the following tasks:
1. If there's a line under the left sensor, turn left
1. If there's a line under the right sensor, turn right
1. If there's no line under the right sensor, drive forwards
1. If there's no line under the left sensor, drive forwards
--- /hint --- --- hint ---
The syntax used in the example program is as follows for the first line:
```python
left_sensor.when_line = robot.left
```
Now try to complete the remaining three lines.
--- /hint --- --- hint ---
Here are the four lines of code you need. If you're running your code from the terminal, you'll need to add `pause()` at the end as well.

```python
left_sensor.when_line = robot.left
right_sensor.when_line = robot.right
left_sensor.when_no_line = robot.forward
right_sensor.when_no_line = robot.forward
                 
pause()
```
--- /hint --- --- /hints ---

Don't worry if you're robot tracks off its line a bit. Just observe if it attempts to stay on the line. Here's an example of a robot running on a basic track with this algorithm.

![final](images/final.gif)
