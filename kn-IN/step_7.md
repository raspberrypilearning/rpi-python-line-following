## ಅಂತಿಮ ಅಲ್ಗಾರಿದಮ್

ಈಗ ನೀವು ಮೋಟಾರ್ ಉಪಯೋಗಿಸುವ ವ್ಯಾಲ್ಯೂ ಗಳನ್ನು output ಮಾಡುತ್ತಿರುವಿರಿ. ಈಗ ನಿಮ್ಮ ವ್ಯಾಲ್ಯೂ ಗಳನ್ನು ಫೀಡ್ ಮಾಡುವ ಸಮಯ.

ಮೊದಲಿಗೆ, ನಿಮ್ಮ `while True` loop ಅನ್ನು **generator** ಆಗಿ ಮಾಡಿ. ಜನರೇಟರ್ ಸ್ವಲ್ಪ ಮಟ್ಟಿಗೆ ಒಂದು function. ಆದರೆ, ಅದು ನಿರಂತರವಾಗಿ run ಆಗುತ್ತದೆ ಮತ್ತು ಕೇವಲ ಕೇಳಿದಾಗ `yield` ವ್ಯಾಲ್ಯೂ ಗಳನ್ನು ನೀಡುತ್ತದೆ.

--- task ---

ನಿಮ್ಮ loop ಅನ್ನು ಈ ರೀತಿಯ ಜನರೇಟರ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ:

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

--- /task ---

ಈಗ ನೀವು ಮಾಡಬೇಕಾಗಿರುವುದು ರೋಬೋಟ್‌ನ ಮೋಟಾರ್ ವ್ಯಾಲ್ಯೂ ಗಳ `source`, ಜನರೇಟರ್‌ನ ಫಲಿತಾಂಶವಾಗಲಿದೆ ಎಂದು ಹೇಳುವುದು.

--- task ---

ಜನರೇಟರ್ ಕೆಳಗೆ ಈ code ಸಾಲನ್ನು ಸೇರಿಸಿ:

```python
robot.source = motor_speed()
```

--- /task ---

ರೋಬೋಟ್ ನಿರಂತರವಾಗಿ run ಆಗದಿರಲು ಮತ್ತು ಎಲ್ಲಾ ಘಟಕಗಳ connection ಗಳನ್ನು ಮುಚ್ಚಲು, ನೀವು ಈ ಸಾಲುಗಳನ್ನು ಸೇರಿಸಬಹುದು:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

--- task ---

ಈಗ ನಿಮ್ಮ code ಅನ್ನು run ಮಾಡಿ, ನಿಮ್ಮ ರೋಬೋಟ್ ಅನ್ನು ಟ್ರ್ಯಾಕ್ ಮೂಲಕ ಪರೀಕ್ಷಿಸಿ.

--- /task ---

ಕೆಲವೊಮ್ಮೆ ರೋಬೋಟ್ ಸ್ವಲ್ಪ ವೇಗವಾಗಿ run ಆಗುತ್ತದೆ. ಆದ್ದರಿಂದ ಈ ಕೆಳಗಿನ ಪೂರ್ಣಗೊಂಡ ಸ್ಕ್ರಿಪ್ಟ್‌ನಲ್ಲಿ ತೋರಿಸಿರುವಂತೆ ನಿಮ್ಮ code ಅನ್ನು ಸ್ವಲ್ಪ ತಿರುಚಬಹುದು. ರೋಬೋಟ್ ಅನ್ನು ಸ್ವಲ್ಪ ನಿಧಾನಗೊಳಿಸಲು ಇದು ಸ್ಪೀಡ್ ಮಲ್ಟಿಪ್ಲೈಯರ್ ಅನ್ನು ಸೇರಿಸುತ್ತದೆ.

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
```
<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> ನಿಮ್ಮ ಬ್ರೌಸರ್ ವೆಬ್‌ಎಂ ವೀಡಿಯೊವನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ Firefox ಅಥವಾ Chrome ಅನ್ನು ಪ್ರಯತ್ನಿಸಿ. </video>