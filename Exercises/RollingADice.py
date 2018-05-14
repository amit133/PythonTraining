import pyttsx3 as pyttsx
import random
from playsound import playsound
from PIL import Image

#engine = pyttsx.init()
#
#engine.say('Lets roll two dice')
#
#engine.runAndWait()
#
#number1 = random.randint(1, 90)
#number2 = random.randint(1, 6)
#
## play a sound file
#playsound('./sound/RollTwoDice.mp3')
#
#rollResult = 'You rolled ' + str(number1) + ' and ' + str(number2)
#engine.say(rollResult)
#print(rollResult)
#engine.runAndWait()

#img = Image.open('./images/200w.webp')
#img.show()


myrange = list(range(1, 6+1))
# get a random number
# if that number was drawn before, get another random number till it doesn't match

play = True
while play and len(myrange) > 1:
	a = random.choice(myrange)
	#print(a)
	myrange.remove(a)
	while True:
		toContinue = input('Do you wish to continue the game (Y/N)? ').lower()
		print(a)
		if toContinue == 'y' or toContinue == "":
			play = True
			break
		elif toContinue == 'n':
			play = False
			break
		else:
			toContinue = input('Enter only Y or N. \n Do you wish to continue the game (Y/N)? ').lower()

print('And the last number is {0}'.format(myrange[0]))			