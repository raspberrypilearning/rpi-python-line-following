## Programming a line following algorithm

**In this example the motor controller board is connected so that the left motor is on pins `7` and `8` and the righ motor is on pins `9` and `10`. The left line sensor is on pin `17` and the right line sensor is on pin `17`**

--- task ---
Open up you prefered text editor or IDE on your Raspberry Pi, and begin by setting up your motor controller board and your sensors, using `gpiozero`

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)
```
--- /task ---

to begin with you can write a really simple line following algorithm, just to test yhat your robot is working.

The `gpiozero` module can call a function depending on whether or not a line has been detected. For example:

```python
left_sensor.when_no_line = function_name_to_call
```

This will tell the robot to do something when the `left_sensor` detects that it is not above a line.
So bby telling the robot to go forward when no line has been detected, but to turn if a line is detected, you can produce very basic line following behaviour.

--- task ---
Add our lines of code to your robot, to produce a basic line following algorith.
--- hints --- --- hint ---
Each line should perform the following tasks:
1. If there's a line under the left sensor - turn left
2. If there's a line under the right sensor - turn right
3. If there's no line under the right sensor - drive forwards
4. If there's no line under the left sensor - drive forwards
--- /hint --- --- hint ---
The syntax used here is as follows for the first line
```python
left_sensor.when_line = robot.left
```
Now try to complete the remianin three lines
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
--- /task ---
