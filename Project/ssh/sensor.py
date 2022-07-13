import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=23
GPIO_ECHO=24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start_time=time.time()
	stop_time=time.time()
	while GPIO.input(GPIO_ECHO) == 0:
		start_time=time.time()
	while GPIO.input(GPIO_ECHO) == 1:
		stop_time=time.time()

	time_elapsed=stop_time - start_time
	distance=(time_elapsed * 34300) / 2

	return distance

def showDistance():

	DangerValue=distance()
	print("DANGER value = {:.2f} cm".format(DangerValue))
	return DangerValue

def early_warning():
	minWarningValue=2.00
	mixWarningValue=103.00
	DANGER=False
	while True:
		distanceValue=showDistance()	
		if (((distanceValue >= minWarningValue) and (distanceValue <= mixWarningValue)) or 
		(distanceValue <= minWarningValue)):
			DANGER=True
			break
			
		else:
			DANGER=False		
	return DANGER




