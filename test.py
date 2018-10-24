from sense_hat import SenseHat
from time import sleep
##from firebase import firebase


sense = SenseHat()
sense.clear()
##firebase = firebase.FirebaseApplication("https://raspberrypi-38859.firebaseio.com/",None)

##results = firebase.post({'Temperature': str(t), 'Pressure': str(h), 'Humidity': str(h)})

p = sense.get_pressure()
t = sense.get_temperature()
h = sense.get_humidity()

p = round(p,1)
t = round(t,1)
h = round(h,1)

blue = (0,0,255)
red = (255,0,0)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

def getData():
	print ("Temperature: " + str(t) + "Pressure: " + str(p) + "Humidity: " + str(h))
	##results

sense.show_message("Program Starting in 3 2 1", scroll_speed = 0.09, text_colour = red)

while True:
	getData()
	sleep(5)



