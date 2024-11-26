## A better line follower

Don't forget to adjust the pin numbers if you've used different GPIO pins.

--- task ---

Create a new file

--- /task --- 

--- task ---

Add the following lines of code and run it. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

while True:
	left_detect  = int(left_sensor.value)
	right_detect = int(right_sensor.value)
	print(left_detect, right_detect)

--- /code ---

--- /task ---

--- task ---

Move the robot back and forth over the line to see what happens.

Check you can see the output from the sensors.

![sensor_output](images/sensor_output.gif)

--- /task ---

--- task ---

Within the `while True` loop, create two new variables called `left_mot` and `right_mot`. These variables should have the same value that you would like the motors to receive. You can simply print out their values within the loop.


--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 12-21
---
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

while True:
	left_detect  = int(left_sensor.value)
	right_detect = int(right_sensor.value)

	if left_detect == 0 and right_detect == 0:
		left_mot = 1
		right_mot = 1

	if left_detect == 0 and right_detect == 1:
		left_mot = -1
	if left_detect == 1 and right_detect == 0:
		right_mot = -1

	print(right_mot, left_mot)

--- /code ---
 
--- /task ---

--- task ---

**Test:** Run your code and see what is printed when you move the robot over the line.

![sensor_output2.gif](images/sensor_output2.gif)

--- /task ---
