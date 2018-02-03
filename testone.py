import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:

        GPIO.output(11,0)
        print "Led on now pin off zero volt  " 
        time.sleep(.80)
        GPIO.output(11,1)
        print "Led on now pin on 3.3 volt "
        time.sleep(.80)
