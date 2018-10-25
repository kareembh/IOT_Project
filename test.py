from sense_hat import SenseHat
from time import sleep
from firebase import firebase


sense = SenseHat()
sense.clear()
firebase = firebase.FirebaseApplication('https://project502-4a209.firebaseio.com/kareem',None)



p = 0.0
t = 0.0
h = 0.0

blue = (0,0,255)
red = (255,0,0)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

def getData():
	p = sense.get_pressure()
	t = sense.get_temperature()
	h = sense.get_humidity()

	p = round(p,1)
	t = round(t,1)
	h = round(h,1)
	print ("Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h))
	sense.clear()
	firebase.post('/kareem', {'Temperature': str(t)})

sense.show_message("Program Starting in 3 2 1", scroll_speed = 0.09, text_colour = red)

while True:
	getData()
	sleep(5)



