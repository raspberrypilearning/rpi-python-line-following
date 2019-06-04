## The final algorithm

Now that you are outputting values that the motors can use, it is time to feed these values in.

To begin with you're going to turn your `while True` loop into a **generator**. A generator is a little like a function, except that it will continually run and only `yield` values when it is asked for them.

\--- task \--- Turn your loop into a generator like this:

```python
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot, left_mot)
```

\--- /task \---

Now all you need to do is to say that the `source` of the robot's motor values is going to be the result of the generator.

\--- task \--- Add in this line of code below the generator:

```python
robot.source = motor_speed()
```

\--- /task \---

To make sure that the robot doesn't keep running forever, and to close all the components connections cleanly, you can optionally add in these lines as well:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

\--- task \--- Now run your code and test your robot over a track. \--- /task \---

Sometimes the robot runs a little too fast, so you can tweak your code a bit as shown in the following completed script. This adds in a speed multiplier to slow the robot down a little.

```python
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
        ## Stage 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot * speed, left_mot * speed)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> Your browser does not support WebM video, so try FireFox or Chrome. </video>