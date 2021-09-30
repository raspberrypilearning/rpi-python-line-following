## अंतिम अल्गोरिदम

मोटर्स वापरू शकतील अशी व्हॅल्यूज आऊटपुट करत असताना आता या व्हॅल्यूज feed (पुरवणे) करायची वेळ आली आहे.

सुरूवातीस आपण आपले `while True` लूप ** generator** (जनरेटर) मध्ये जोडा. जनरेटर हे थोडेसे फंक्शनसारखे असते, हे सतत चालते आणि केवळ ` yield ` मूल्य विचारले जाते तेव्हाच मूल्ये देते.

\--- task \---

याप्रमाणे जनरेटरमध्ये आपला लूप बदला:

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

आता आपल्याला फक्त असे म्हणायचे आहे की `source` रोबोटच्या मोटर व्हॅल्यूज जनरेटर व्हॅल्यूजचा परिणाम असेल.

\--- task \---

जनरेटरच्या खाली या ओळीत code जोडा:

```python
robot.source = motor_speed()
```

\--- /task \---

रोबोट कायमचा चालू राहणार नाही हे सुनिश्चित करण्यासाठी आणि सर्व घटक कनेक्शन बंद करण्यासाठी आपण या ओळींमध्ये या ओळी देखील जोडू शकता:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

\--- task \---

आता आपला code चालवा आणि ट्रॅकवर आपल्या रोबोटची चाचणी घ्या.

\--- /task \---

कधीकधी रोबोट थोडा वेगात धावतो, जेणेकरून आपण पुढील पूर्ण झालेल्या स्क्रिप्टमध्ये दर्शविल्यानुसार आपला कोड थोडा बदल करू शकता. वेग गुणक रोबोट चा वेग थोडेसे कमी करण्यासाठी मदत करू शकता.

```python
rom gpiozero import Robot, LineSensor
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
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> आपला ब्राउझर वेबएम व्हिडिओस समर्थन देत नाही, म्हणून FireFox किंवा Chrome वापरून पहा. </video>