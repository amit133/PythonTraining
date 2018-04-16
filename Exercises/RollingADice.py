import pyttsx3 as pyttsx
import random
from playsound import playsound
from PIL import Image

engine = pyttsx.init()

engine.say('Lets roll two dice')

engine.runAndWait()

number1 = random.randint(1, 6)
number2 = random.randint(1, 6)

# play a sound file
playsound('./sound/RollTwoDice.mp3')

rollResult = 'You rolled ' + str(number1) + ' and ' + str(number2)
engine.say(rollResult)
print(rollResult)
engine.runAndWait()

img = Image.open('./images/200w.webp')
img.show()

