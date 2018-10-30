## Imported Modules
from sense_hat import SenseHat
from time import sleep
from firebase import firebase

##Module variables
sense = SenseHat()
sense.clear()
firebase = firebase.FirebaseApplication('https://project502-4a209.firebaseio.com/kareem',None)

## Sensor variables
p = 0.0 ##p for pressure
t = 0.0 ## t for temperature
h = 0.0 ## h for humidity

## Colour variables in rgb
blue = (0,0,255)
red = (255,0,0)

## Message variable
message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

## GetData function defined
def getData():
	p = sense.get_pressure()
	t = sense.get_temperature()
	h = sense.get_humidity()

	p = round(p,1)
	t = round(t,1)
	h = round(h,1)
	print ("Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h))
	sense.clear()
	firebase.post('/kareem', {'Temperature': str(t), 'Pressure': str(p), 'Humidity': str(h)})

## Displays program starting message
sense.show_message("Program Starting in 3 2 1", scroll_speed = 0.09, text_colour = red)

## Program running Sequence
while True:
	getData()
	sleep(10)
