from gpiozero import PWMOutputDevice as pwm
import time

servo = pwm(11,frequency=50) # BRODCOM PIN NUMBERING!!!

x = float(0.025) # python for loops suck
while x < 0.125: # some servos use different dutycycles,
                 # these are the most common values
    servo.value = (x)   # 50Hz (20ms between pulses)
    print(servo.value)  # 0.025% (0.5ms) = 0 deg
    x += 0.001          # 0.125% (2.5ms) = 180 deg
    
    time.sleep(0.1)

