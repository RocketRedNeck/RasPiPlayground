# Create new class called Servo

class servo:
    #import RPi.GPIO
    #RPi.GPIO.setmode(GPIO.BOARD)

    # Initialize servo on <channel>
    # Use referenceName = servo(channel)
    def __init__(self, channel):
        self.channel = channel
        self.pos = 0
        self.dutyCycle = (self.pos / 18) + 2.5

        import RPi.GPIO
        
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.cleanup(self.channel) # remove anything already there
        RPi.GPIO.setup(self.channel, RPi.GPIO.OUT) # set as output       
        
    # Write servo to pos
    def write(self, pos):
        self.pos = pos
        self.dutyCycle = (self.pos / 18) + 2.5
        
        import RPi.GPIO
        import time
        
        self.pwm = RPi.GPIO.PWM(self.channel, 50) # make <self> pwm object

        self.pwm.start(self.dutyCycle) # start pwm
        time.sleep(0.2)
        self.pwm.stop()

    # Write servo to specific duty cycle
    def writeDutyCycle(self, dutyCycle):
        self.dutyCycle = dutyCycle
        
        import RPi.GPIO
        import time
        
        self.pwm = RPi.GPIO.PWM(self.channel, 50) # make <self> pwm object

        self.pwm.start(self.dutyCycle) # start pwm
        time.sleep(0.2)
        self.pwm.stop()


    # Return servo's channel
    def getChannel(self):
        return(self.channel)

    # Return servo's position
    def read(self):
        return(self.pos)

    # Return servo's duty cycle
    def duty_cycle(self):
        return(self.dutyCycle)

    # Detatches servo so pin can be reused
    def detach(self):
        import RPi.GPIO
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.cleanup(self.channel)

        
        
