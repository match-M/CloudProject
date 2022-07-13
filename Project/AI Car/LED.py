import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) ##信号引脚模式定义，使用.BCM模式
LED0 = 10 ##LED0 的IO口定义
LED1 = 9  ##LED1 的IO口定义
LED2 = 25 ##LED2 的IO口定义
GPIO.setwarnings(False)
GPIO.setup(LED0,GPIO.OUT,initial = GPIO.HIGH) ##初始化
GPIO.setup(LED1,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(LED2,GPIO.OUT,initial = GPIO.HIGH)
def init_light():
    GPIO.output(LED0,False)
    GPIO.output(LED1,False)
    GPIO.output(LED2,False)
    time.sleep(0.5)
    GPIO.output(LED0,True)
    GPIO.output(LED1,False)
    GPIO.output(LED2,False)
    time.sleep(0.5)
    GPIO.output(LED0,False)
    GPIO.output(LED1,True)
    GPIO.output(LED2,False)
    time.sleep(0.5)
    GPIO.output(LED0,False)
    GPIO.output(LED1,False)
    GPIO.output(LED2,False)
    time.sleep(0.5)
    GPIO.output(LED0,True)
    GPIO.output(LED1,True)
    GPIO.output(LED2,True)
    time.sleep(0.5)
while True:
    init_light()