## Planning a better algorithm

The previous algorithm might be OK, it can easily be improved upon. Let's see what a better algorithm might look like!

When a line sensor is above a line, it outputs a `1`. When it's off a line, it outputs a `0`.

The robot, whenever it receives a `1` signal to the right motor, it drives that motor forwards. When it receives a `-1`, it drives the motor backwards.

Let's have a look at an algorithm that takes into account the position of the robot, the states of the lines sensors, and the actions required of the motors.

1. The robot is perfectly on the line and should drive forwards:
   - Both line sensors are off the line and outputting a `0`
   - Both motors should receive `1` to drive forwards
   
2. The robot has drifted left and needs to turn right:
   - The right sensor is on the line and outputting a `1`
   - The left sensor is off the line and outputting a `0`
   - The left motor should run backwards and so receive a `-1`
   - The right motor should run forwards and so receive a `1`
   
3. The robot has drifted right and needs to turn left:
   - The right sensor is off the line and outputting a `0`
   - The left sensor is on the line and outputting a `1`
   - The Left motor should run forwards and so receive a `1`
   - The right motor should run backwards and so receive a `-1`
   
How can you make this happen in code? First of all, you'll create an infinite loop to view the sensor values.

--- task ---
In a new file, add in the following lines of code and run it. Don't forget to adjust the pin numbers if you've used different GPIO pins.

```python
from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

while True:
	left_detect  = int(left_sensor.value)
	right_detect = int(right_sensor.value)
	print(left_detect, right_detect)
```
Now move the robot back and forth over the line to see what happens.
--- /task ---

Hopefully, you should see the binary output from the sensors.

![sensor_output](images/sensor_output.gif)

So now that you have the sensor output, you need to alter it a little before you send it to the motors. As per the algorithm above:
- If both sensors output `0`, then both motors should receive `1`
- If the right sensor outputs `1`, then the left motor should receive `-1`
- If the left sensor outputs `1`, then the right motor should receive `-1`

--- task ---

Within the `while True` loop, create two new variables called `left_mot` and `right_mot`. These variables should have the same value that you would like the motors to receive. You can simply print out their values within the loop.

--- /task ---

--- hints --- --- hint ---
According to the above algorithm, `if left_detect == 0 and right_detect == 0:`, what do you want the values of `left_mot` and `right_mot` to be?
--- /hint --- --- hint ---
Here's the code for the first condition:
```
while True:
	left_detect  = int(left_sensor.value)
	right_detect = int(right_sensor.value)
	if left_detect == 0 and right_detect == 0:
		left_mot = 1
		right_mot = 1
```
You need two more `if` statements to handle the sensors being triggered by a line.
--- /hint --- --- hint ---
Here's the completed code, with the print statements:
```python
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
 ```
--- /hint --- --- /hints ---

--- task ---
When you are done, run your code and test how it works when you move the robot over the line.
![sensor_output2.gif](images/sensor_output2.gif)
--- /task ---
