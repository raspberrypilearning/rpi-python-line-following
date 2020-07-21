## अंतिम एल्गोरिथ्म

अब जब आप उन मानों को आउटपुट कर रहे हैं जिनका उपयोग मोटर्स कर सकते हैं, तो इन मूल्यों को फीड करने का समय आ गया है।

शुरू करने के लिए आप एक `जनरेटर` में अपने**while True**लूप को चालू करने जा रहे हैं । एक जनरेटर थोड़ा बहुत एक फ़ंक्शन की तरह है, सिवाय इसके कि यह लगातार run करेगा और केवल मान `फल देगा` जब यह उनके लिए कहा जाता है।

--- task ---

अपने लूप को इस तरह जनरेटर में बदलें:

```python
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## चरण 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## चरण 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        #print(r, l)
        yield (right_mot, left_mot)
```

--- /task ---

अब आपको केवल इतना कहना है कि रोबोट के मोटर मान का `स्रोत` जनरेटर का परिणाम होने जा रहा है।

--- task ---

जनरेटर के नीचे कोड की इस पंक्ति में जोड़ें:

```python
robot.source = motor_speed()
```

--- /task ---

यह सुनिश्चित करने के लिए कि रोबोट हमेशा के लिए चालू नहीं रहता है, और सभी घटकों के कनेक्शन को सफाई से बंद करने के लिए, आप इच्छित रूप से इन पंक्तियों में जोड़ सकते हैं:

```python
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
```

--- task ---

अब अपना कोड Run करें और एक ट्रैक पर अपने रोबोट का परीक्षण करें।

--- /task ---

कभी-कभी रोबोट थोड़ा बहुत तेज चलता है, इसलिए आप अपने कोड को थोड़ा मोड़ सकते हैं जैसा कि निम्नलिखित पूरी स्क्रिप्ट में दिखाया गया है। यह रोबोट को थोड़ा धीमा करने के लिए एक गति गुणक में जोड़ता है।

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
        ## चरण 1
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## चरण 2
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

<video width="640" height="360" controls> 
<source src="images/showcase.webm" type="video/webm"> 
आपका ब्राउज़र WebM वीडियो का समर्थन नहीं करता है, FireFox या Chrome आज़माएँ 
</video>


***
इस परियोजना का अनुवाद स्वयंसेवकों ने किया:

Jaspreet Singh

Vaishali Anand

स्वयंसेवकों को धन्यवाद, हम दुनिया भर के लोगों को अपनी भाषा में सीखने का मौका दे सकते हैं। आप स्वेच्छा से अधिक लोगों तक पहुँचने में मदद कर सकते हैं - [rpf.io/translate](https://rpf.io/translate) पर अधिक जानकारी प्राप्त करें।