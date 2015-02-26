#Description: rpiMotionSensor waits for input from a connected motion sensor. When input is received,
#output is written to a GPIO where an LED is (hopefully) connected. When the motion sensor is no longer
#active, then we write 0 to the led.
import RPi.GPIO as GPIO
import time
#set up GPIO using BCM numbering

GPIO.setmode(GPIO.BCM)

ledpin = 23
motionSensorInPin = 4

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(ledpin,GPIO.OUT)

def ledOff():
    print("Led on")
    GPIO.output(ledpin,False)
    

def ledOn():
    print("Led off")
    GPIO.output(ledpin,True)


def motionDetected(channel):
    print("Motion has been detected.")
    ledOn()

GPIO.add_event_detect(motionSensorInPin, GPIO.RISING, callback=motionDetected, bouncetime=300)

#subscribe to callback function on motionSensorInPin
while True:
    print("Waiting for motion...")
    time.sleep(1)

GPIO.remove_event_detect(motionSensorInPin)
GPIO.cleanup()