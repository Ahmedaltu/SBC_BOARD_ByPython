from gpio import *
from time import *

def main():
	while True:
		motion_sensor = digitalRead(9)
		if motion_sensor == HIGH:
			print('Motion Detected')

			customWrite(2,2) # Light on
			delay(5000)    # wait 

			customWrite(2,0)  # Light off



if __name__ == "__main__":
	main()
