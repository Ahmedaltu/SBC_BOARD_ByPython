# make the LED blinking

from gpio import *
from time import *

def main():
	pinMode(1, OUT)      # output for D1 (Pin1) for the LED
	print("Blinking")
	while True:
		digitalWrite(1, HIGH);      # (1 = Pin num 1, Hight = on)   for the LED becaues it is connected throught pin 1
		customWrite(0, 127);        #  ( pin 0, in 127 direction)   make the servo motor go to positive 127 direction
		delay(1000)                 # wait for 1000 milli second
		digitalWrite(1, LOW);      # (1 = Pin num 1, LOW = off)
		customWrite(0, -127);       # ( pin 0, in -127 direction)   make the servo motor go to negetive 127 direction
		delay(500)

if __name__ == "__main__":
	main()