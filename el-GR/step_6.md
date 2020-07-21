## Σχεδίασε έναν καλύτερο αλγόριθμο

Ο προηγούμενος αλγόριθμος μπορεί να είναι εντάξει, αλλά μπορεί επίσης εύκολα να βελτιωθεί. Ας δούμε πώς θα μπορούσε να μοιάζει ένας καλύτερος αλγόριθμος!

Όταν ένας αισθητήρας γραμμής είναι πάνω από μια γραμμή, εμφανίζει ένα `1`. Όταν είναι εκτός γραμμής, εμφανίζει ένα `0`.

Οι κινητήρες λειτουργούν ελαφρώς διαφορετικά: το ρομπότ, όποτε λαμβάνει σήμα `1` προς το δεξιό κινητήρα, οδηγεί αυτόν τον κινητήρα προς τα εμπρός. Όταν λαμβάνει σήμα `-1`, οδηγεί τον κινητήρα προς τα πίσω.

Ας ρίξουμε μια ματιά σε έναν αλγόριθμο που λαμβάνει υπόψη τη θέση του ρομπότ, τις καταστάσεις των αισθητήρων γραμμών και τις ενέργειες που απαιτούνται από τους κινητήρες.

1. Το ρομπότ είναι τέλεια πάνω στη γραμμή και πρέπει να προχώρησει προς τα εμπρός:
    
    - Και οι δύο αισθητήρες γραμμής είναι εκτός γραμμής και εμφανίζουν `0`
    - Και οι δύο κινητήρες θα πρέπει να λαμβάνουν `1` για να προχωρήσουμε προς τα εμπρός

2. Το ρομπότ έχει μετακινηθεί αριστερά και πρέπει να στρίψει δεξιά:
    
    - Ο δεξιός αισθητήρας βρίσκεται πάνω στη γραμμή και εμφανίζει `1`
    - Ο αριστερός αισθητήρας είναι εκτός γραμμής και εμφανίζει `0`
    - Ο αριστερός κινητήρας πρέπει να πάει προς τα πίσω και έτσι λαμβάνει `-1`
    - Ο δεξιός κινητήρας πρέπει να κινηθεί προς τα εμπρός και έτσι λαμβάνει `1`

3. Το ρομπότ έχει μετακινηθεί δεξιά και πρέπει να στρίψει αριστερά:
    
    - Ο δεξιός αισθητήρας είναι εκτός γραμμής και εμφανίζει `0`
    - Ο αριστερός αισθητήρας είναι πάνω στη γραμμή και εμφανίζει `1`
    - Ο αριστερός κινητήρας πρέπει να κινηθεί προς τα εμπρός και έτσι λαμβάνει `1`
    - Ο δεξιός κινητήρας πρέπει να πάει προς τα πίσω και έτσι λαμβάνει `-1`

Πώς μπορείς να το αποτυπώσεις αυτό σε κώδικα; Αρχικά, θα δημιουργήσεις έναν άπειρο βρόχο για να βλέπεις τις τιμές των αισθητήρων.

\--- task \---

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

\--- /task \---

Hopefully, you should see the binary output from the sensors.

![sensor_output](images/sensor_output.gif)

So now that you have the sensor output, you need to alter it a little before you send it to the motors. As per the algorithm above:

- Εάν και οι δύο αισθητήρες εξάγουν `0` , τότε και οι δύο κινητήρες πρέπει να λαμβάνουν `1`
- Εάν ο δεξιός αισθητήρας εξάγει `1` , τότε ο αριστερός κινητήρας πρέπει να λάβει `-1`
- Εάν ο αριστερός αισθητήρας εξάγει `1` , τότε ο δεξιός κινητήρας πρέπει να λάβει `-1`

\--- task \---

Within the `while True` loop, create two new variables called `left_mot` and `right_mot`. These variables should have the same value that you would like the motors to receive. You can simply print out their values within the loop.

\--- /task \---

\--- hints \--- \--- hint \---

According to the above algorithm, `if left_detect == 0 and right_detect == 0:`, what do you want the values of `left_mot` and `right_mot` to be?

\--- /hint \--- \--- hint \---

Here's the code for the first condition:

    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
    

You need two more `if` statements to handle the sensors being triggered by a line.

\--- /hint \--- \--- hint \---

Here's the completed code, with the print statements:

```python while True: left_detect = int(left_sensor.value) right_detect = int(right_sensor.value)

    if left_detect == 0 and right_detect == 0:
        left_mot = 1
        right_mot = 1
    
    if left_detect == 0 and right_detect == 1:
        left_mot = -1
    if left_detect == 1 and right_detect == 0:
        right_mot = -1
    
    print(right_mot, left_mot)
    

```

\--- /hint \--- \--- /hints \---

\--- task \---

When you are done, run your code and test how it works when you move the robot over the line.

![sensor_output2.gif](images/sensor_output2.gif)

\--- /task \---