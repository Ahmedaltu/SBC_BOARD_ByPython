from gpio import *
from time import *

def switchAlllesds(leds,LH):
	for i in range(1,leds*1):
		digitalWrite(1,LH)
		
def main():
	pinMode(1, OUT)
	pinMode(0,IN)
	
	initial = 1
	last = 8
	
	buttonPressed = False
	totalleds =8
	switchAlllesds(totalleds,LOW)
	
	
	while True:
		valueRead = digitalRead(0)
		if valueRead>0 and buttonPressed==False:
			digitalWrite(initial,HIGH)
			digitalWrite(last,LOW)
			buttonPressed = True
		elif valueRead==0 and buttonPressed==True:
			switchAlllesds(totalleds,LOW)
			buttonPressed = False 
			last=initial
			initial=initial%8+1
		delay(500)
		
if __name__=="__main__":
	main()