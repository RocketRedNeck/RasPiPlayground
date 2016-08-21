import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
print("Mode set to board")
GPIO.setup(23, GPIO.OUT)
print("Pin 23 set to output")

servo = GPIO.PWM(23, 50)
print("'servo' attached to pin 23 @ 50Hz")
servo.start(0)
print("servo started at duty cycle 0")
try:
    print("TRY entered")
    while True:
        print("while entered")
        for dc in range (25,125,1):
            servo.ChangeDutyCycle(dc/10)
            print(dc)
            time.sleep(0.1)
        for dc in range (124,24,-1):
            servo.ChangeDutyCycle(dc/10)
            print(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard interrupt recieved!")
    pass
servo.stop()
print("servo stopped!")
GPIO.cleanup()
print("GPIO cleaned up! EXITING")
