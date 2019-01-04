## Γράψε έναν αλγόριθμο για να ακολουθεί το ρομπότ τη γραμμή

**Σημείωση:** Σε αυτό το παράδειγμα, η πλακέτα ελέγχου κινητήρα είναι συνδεδεμένη έτσι ώστε ο αριστερός κινητήρας να βρίσκεται στα pin **GPIO 7** και **GPIO 8** , και ο δεξιός κινητήρας να βρίσκεται στα pin **GPIO 9** και **GPIO 10** . Ο αριστερός αισθητήρας γραμμής βρίσκεται στο pin **GPIO 17**, και ο δεξιός αισθητήρας γραμμής βρίσκεται στο pin **GPIO 27**.

\--- task \--- Open up your preferred text editor or IDE on your Raspberry Pi, and begin by setting up your motor controller board and your sensors using `gpiozero`:

```python
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10)) 
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)
```

\--- /task \---

Αρχικά, γράψε έναν πολύ απλό αλγόριθμο, μόνο για να ελέγξεις ότι το ρομπότ σου λειτουργεί.

Το `gpiozero` μπορεί να καλέσει μια συνάρτηση ανάλογα με το αν έχει ανιχνευθεί ή όχι μια γραμμή. Για παράδειγμα:

```python
left_sensor.when_no_line = function_name_to_call
```

Αυτό θα πει στο ρομπότ να κάνει κάτι όταν ο `αριστερός αισθητήρας (left_sensor)` ανιχνεύσει ότι δεν είναι πάνω από μια γραμμή. Λέγοντας στο ρομπότ να προχωρήσει όταν δεν έχει εντοπιστεί καμία γραμμή, αλλά να γυρίσει αν εντοπιστεί μια γραμμή, μπορείς να δημιουργήσεις μία πολύ βασική συμπεριφορά οδήγησης με βοήθεια γραμμής.

\--- task \--- Πρόσθεσε τέσσερις γραμμές κώδικα στο πρόγραμμα του ρομπότ σου για να δημιουργήσεις έναν βασικό αλγόριθμο.

\--- /task \---

\--- hints \--- \--- hint \--- The lines should perform the following tasks:

1. If there's a line under the left sensor, turn left
2. If there's a line under the right sensor, turn right
3. If there's no line under the right sensor, drive forwards
4. If there's no line under the left sensor, drive forwards \--- /hint \--- \--- hint \--- The syntax used in the example program is as follows for the first line:

```python
left_sensor.when_line = robot.left
```

Now try to complete the remaining three lines. \--- /hint \--- \--- hint \--- Here are the four lines of code you need. If you're running your code from the terminal, you'll need to add `pause()` at the end as well.

```python
left_sensor.when_line = robot.left
right_sensor.when_line = robot.right
left_sensor.when_no_line = robot.forward
right_sensor.when_no_line = robot.forward

pause()
```

\--- /hint \--- \--- /hints \---

Don't worry if you're robot tracks off its line a bit. Just observe if it attempts to stay on the line. Here's an example of a robot running on a basic track with this algorithm.

![final](images/final.gif)