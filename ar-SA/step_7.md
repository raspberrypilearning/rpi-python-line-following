## الخوارزمية النهائية

الآن أنت تخرج القيم التي يمكن للمحركات استخدامها، لذا حان الوقت لتغذية هذه القيم فيها.

لتبدأ ، ستقوم بتحويل الحلقة التكرارية `while True ` إلى **مولد**. المولد يشبه الدالة قليلاً, باستثناء أنه سيبقى يعمل بشكل مستمر و فقط `ينتج` قيم عندما يطلب منه ذلك.

\--- task \---

حول الحلقة التكرارية إلى مولد كالتالي:

```python
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## المرحلة 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## المرحلة 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot, left_mot)
```

\--- /task \---

الآن كل ما عليك فعله هو أن تقول أن `المصدر` لقيم محرك الروبوت ستكون نتيجة المولد.

\--- task \---

أضف هذا السطر من الكود أسفل المولد:

```python
robot.source = motor_speed()
```

\--- /task \---

للتأكد من أن الروبوت لا يستمر في العمل إلى الأبد ، ولإغلاق جميع أتصالات المكونات بشكل نظيف ، يمكنك أيضاً إضافة هذه السطور اختياريًا:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

\--- task \---

الآن قم بتشغيل الكود الخاص بك واختبر الروبوت الخاص بك على مسار.

\--- /task \---

في بعض الأحيان يعمل الروبوت بسرعة كبيرة، لذا يمكنك تعديل التعليمات البرمجية قليلاً كما هو موضح في الكود الكامل التالي. هذا يضيف سرعة مضاعفة لإبطاء الروبوت قليلاً.

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
        ## المرحلة 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## المرحلة 2
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
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> لا يدعم متصفحك فيديو WebM ، لذلك جرّب FireFox أو Chrome. </video>