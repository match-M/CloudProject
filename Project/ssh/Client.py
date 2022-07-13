import socket
import time
import os
import RPi.GPIO as GPIO

#TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.88.238", 9000))
#GPIO
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
#TCP
def TcpExcept():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.88.238", 9000))
#TCP and GPIO
def TcpClient():
	while True:
		minWarningValue=2.00
		mixWarningValue=224.00
		DANGER=False
		while True:
			DangerValue=distance()
			print("DANGER value = {:.2f} cm".format(DangerValue))

			distanceValue=distance()	
			if ((distanceValue >= minWarningValue) and (distanceValue < mixWarningValue)):
				DANGER=True
				Value = "True"+' '+distanceValue
				s.send(Value)
				data = s.recv(10485760).decode()
				print(data)
				
			else:
				DANGER=False
while True:
	try:
		try:
			TcpClient()
		except socket.error as e:
		
			print("Waiting...")
			TcpExcept()

	except KeyboardInterrupt:
		print('\n')
		break
s.close()
#while True:
#       try:
#               TcpClient()
#       except KeyboardInterrupt:
#               break

#/home/pi/early_warning_system
