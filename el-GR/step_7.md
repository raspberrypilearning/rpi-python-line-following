## Ο τελικός αλγόριθμος

Τώρα που εμφανίζεις τιμές που μπορούν να χρησιμοποιήσουν οι κινητήρες, μπορείς να τους τις δώσεις.

Για να ξεκινήσουμε θα μετατρέψεις το βρόχο σου `while True` σε μία **γεννήτρια (generator)**. Μια γεννήτρια είναι κάτι σαν μια συνάρτηση, εκτός από το ότι θα τρέχει συνεχώς και θα `επιστρέφει` τιμές όταν της ζητηθεί.

\--- task \--- Κανε τον βρόχο σου γεννήτρια όπως παρακάτω:

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

Τώρα το μόνο που χρειάζεται να κάνεις είναι να πεις ότι η `πηγή (source)` των τιμών του κινητήρα του ρομπότ θα είναι το αποτέλεσμα της γεννήτριας.

\--- task \--- Πρόσθεσε σε αυτή τη γραμμή κώδικα κάτω από τη γεννήτρια:

```python
robot.source = motor_speed()
```

\--- /task \---

Για να βεβαιωθείς ότι το ρομπότ δεν συνεχίζει να τρέχει για πάντα και να κλείσεις καθαρά όλες τις συνδέσεις των εξαρτημάτων, μπορείς επίσης να προσθέσεις και αυτές τις γραμμές:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

\--- task \--- Τώρα εκτέλεσε τον κώδικα σου και δοκίμασε το ρομπότ σου πάνω σε μία διαδρομή. \--- /task \---

Μερικές φορές το ρομπότ τρέχει λίγο περισσότερο γρήγορα, οπότε μπορείς να πειράξεις τον κώδικα λίγο όπως φαίνεται στο παρακάτω ολοκληρωμένο script. Αυτό πειράζει λίγο την ταχύτητα για να επιβραδύνει λίγο το ρομπότ.

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
```<video width="640" height="360" controls> <source src="images/showcase.webm" type="video/webm"> Το πρόγραμμα περιήγησής σου δεν υποστηρίζει βίντεο WebM, επομένως δοκίμασε το FireFox ή το Chrome. </video>