import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
ENA = 13
ENB = 20
IN1 = 19
IN2 = 16
IN3 = 21
IN4 = 26
GPIO.setup(ENA,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial = GPIO.LOW)
def Motor_Forward():
    print("motor forward")
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
def Motor_Backward():
    print("motor Backward")
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
def Motor_TurnLeft():
    print("motor turnleft")
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
def Motor_TrunRight():
    print("motor trunright")
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
def Motor_Stop():
    print("motor stop")
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
while True:
    Motor_Forward()
    time.sleep(1)
    Motor_Backward()
    time.sleep(1)
    Motor_TurnLeft()
    time.sleep(1)
    Motor_TrunRight()
    time.sleep(1)
    