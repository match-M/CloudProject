import RPi.GPIO as GPIO
import time as t

pins = {0:13,1:15}
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pins[0],GPIO.OUT)
GPIO.setup(pins[1],GPIO.OUT)

f = l = False

def redClick():
    global f
    f = False
    GPIO.setup(pins[0],GPIO.HIGH)
    GPIO.setup(pins[1],GPIO.LOW)

def greenClick():
    global f
    f = False
    GPIO.setup(pins[0],GPIO.LOW)
    GPIO.setup(pins[1],GPIO.HIGH)

def stopClick():
    global f
    f = False
    GPIO.setup(pins[0],GPIO.LOW)
    GPIO.setup(pins[1],GPIO.LOW)
    GPIO.cleanup()
    exit()

for i in range(100):
    redClick()
    t.sleep(1)
    greenClick()

stopClick()
