## एक बेहतर एल्गोरिदम की योजना बनाएं

पिछला एल्गोरिथ्म ठीक हो सकता है, पर इसे आसानी से सुधारा जा सकता है। आइए देखें कि एक बेहतर एल्गोरिदम कैसा दिख सकता है!

जब एक लाइन सेंसर एक लाइन से ऊपर होता है, तो यह एक `1` आउटपुट देता है। जब यह एक लाइन से बाहर हो जाता है, तो यह एक `0` आउटपुट देता है।

हालांकि, मोटर्स थोड़ा अलग तरीके से काम करता है: रोबोट, जब भी यह दाएं मोटर को एक `1` संकेत प्राप्त करता है, उस मोटर को आगे की ओर चलाता है। जब यह एक `-1` प्राप्त करता है, यह मोटर को पीछे की ओर चलाता है।

आइए एक एल्गोरिथ्म पर एक नज़र डालें जो रोबोट की स्थिति, लाइनों के सेंसर की स्थिति और मोटर्स की आवश्यक क्रियाओं को ध्यान में रखता है।

1. रोबोट पूरी तरह से लाइन पर है और आगे की ओर ड्राइव करना चाहिए:
    
    - दोनों लाइन सेंसर लाइन से दूर हैं और `0` आउटपुट दे रहे हैं
    - दोनों मोटर्स को आगे बढ़ने के लिए `1` प्राप्त होना चाहिए

2. रोबोट बाईं ओर चला गया है और दाएं मुड़ने की जरूरत है:
    
    - दायां सेंसर लाइन पर है और `1` आउटपुट दे रहा है
    - बाएं सेंसर लाइन से दूर है और `0` आउटपुट दे रहा है
    - बाईं मोटर को पीछे की ओर चलाना चाहिए और इसलिए ` -1` प्राप्त करना चाहिए
    - दाएं मोटर को आगे की ओर चलाना चाहिए और इसलिए `1` प्राप्त करना चाहिए

3. रोबोट दाईं ओर चला गया है और उसे बाएं मुड़ने की जरुरत है:
    
    - दायां सेंसर लाइन से दूर है और `0` आउटपुट दे रहा है
    - बाएं सेंसर लाइन पर है और `1`आउटपुट दे रहा है
    - बाएं मोटर को आगे की ओर run करना चाहिए और इसलिए `1` प्राप्त करना चाहिए
    - दायां मोटर को पीछे की ओर run करना चाहिए और इसलिए ` -1` प्राप्त करना चाहिए

आप इसे कोड में कैसे बना सकते हैं? सबसे पहले, आप सेंसर मूल्यों को देखने के लिए एक अनंत लूप बनाएंगे।

\--- task \---

एक नई फ़ाइल में, कोड की निम्नलिखित पंक्तियों में जोड़ें और इसे चलाएं। यदि आपने विभिन्न GPIO पिन का उपयोग किया है तो पिन नंबर नियमित करना न भूलें।

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

अब रोबोट को आगे-पीछे घुमाएँ और देखें कि क्या होता है।

\--- /task \---

उम्मीद है, आपको सेंसर से बाइनरी आउटपुट देखना चाहिए।

![sensor_output](images/sensor_output.gif)

इसलिए अब जब आपके पास सेंसर आउटपुट है, तो आपको इसे मोटर्स में भेजने से पहले इसे थोड़ा बदलना होगा। ऊपर दिए गए एल्गोरिदम के अनुसार:

- यदि दोनों सेंसर `0` आउटपुट दे रहे है, तो दोनों मोटर्स को `1` प्राप्त करना चाहिए
- यदि दायां सेंसर `1` आउटपुट देता है, फिर बाईं मोटर को `-1` प्राप्त करना चाहिए
- यदि बाएं सेंसर `1` आउटपुट देता है, तो दायां मोटर को `-1` प्राप्त करना चाहिए

\--- task \---

`while True` लूप के अंदर दो नए वैरिएबल बनाएं `left_mot` और `right_mot` । इन वेरिएबल का वही मूल्य होना चाहिए जो आप मोटर्स को प्राप्त करना चाहते हैं। आप सरलता से लूप के भीतर उनके मूल्यों को प्रिंट कर सकते हैं।

\--- /task \---

\--- hints \--- \--- hint \---

उपरोक्त एल्गोरिथ्म के अनुसार, `if left_detect == 0 and right_detect == 0:`, आप `left_mot` और `right_mot` के क्या मुल्य रखना चाहते है?

\--- /hint \--- \--- hint \---

यहाँ पहली शर्त के लिए कोड है:

    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
    

आपको एक लाइन द्वारा चालू किए जा रहे सेंसर को संभालने के लिए दो और `if` बयान चाहिए।

\--- /hint \--- \--- hint \---

यहां प्रिंट कथनों के साथ पूरा कोड दिया गया है:

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

जब आपका हो जाए, तो अपना कोड run करें और परीक्षण करें कि जब आप रोबोट को लाइन में ले जाते हैं तो यह कैसे काम करता है।

![sensor_output2.gif](images/sensor_output2.gif)

\--- /task \---