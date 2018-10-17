from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

p = sense.get_pressure()
t = sense.get_temperature()
h = sense.get_humidity()

p = round(p,1)
t = round(t,1)
h = round(h,1)

blue = (0,0,255)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

sense.show_message(message, scroll_speed = 0.09, text_colour = blue)