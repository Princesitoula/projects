# TEXT TO SPLEECH

from gtts import gTTS
import os

# This project is made by Prince Sitoula

txt = input("Enter your text here:" )
speech = gTTS(text=txt, lang='en')
speech.save("text-to-speech.mp3")
os.system("start text-to-speech.mp3")