import RPi.GPIO as GPIO

import time

Buzzer = 11



CM = [0, 330, 350, 393, 441, 495, 556, 624] #定义频率

song_3 = [ CM[1],CM[1],CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],

CM[3],CM[2],CM[2],CM[1],CM[5],CM[5],CM[4],CM[4],CM[3],CM[3],

CM[2],CM[5],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],CM[1],CM[1],

CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],

CM[2],CM[1],]



beat_3 = [ 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,

0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,]

def setup():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(Buzzer, GPIO.OUT)

    global Buzz

    Buzz = GPIO.PWM(Buzzer, 440)

    Buzz.start(50)


def loop():

    while True:

        print('\n Playing song 3...')

        for i in range(1, len(song_3)):

            Buzz.ChangeFrequency(song_3[i])

            time.sleep(beat_3[i])
def destory():

    Buzz.stop()

    GPIO.output(Buzzer, 1)

    GPIO.cleanup()



if __name__ == '__main__':

    setup()

    try:

        loop()

    except KeyboardInterrupt:

        executed.

        destory()
