import os
import RPi.GPIO as GPIO
import time
from smbus import SMBus
XRservo = SMBus(1)
while True:
    for i in range(180):
        XRservo.XiaoRGEEK_SetServo(1,i)
        time.sleep(0.01)
    for i in range(180):
        XRservo.XiaoRGEEK_SetServo(1,180-i)
        time.sleep(0.01)