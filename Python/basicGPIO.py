# see https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
# for more info, tutorials, and libraries.

# import the GPIO library
import RPi.GPIO as GPIO

# set the pin numbering to board pin numbers
# this is universaly compatable w/ all boards
# so you won't have to change wiring.
# Hardware Note: The GPIO cable flips the GPIO
# pins, so the pins on the outside of the board
# will be on the inside of the cable, and vica versa.
GPIO.setmode(GPIO.BOARD)

# it is possible to have more than 1 program access the
# same channels. so when RPi.GPIO detects a pin configured
# to something other than the default (input), a warning
# is thrown when you try to configure your script
# use GPIO.setwarnings(Flase) to disable this

# all channles must be configured before use, do this with
# GPIO.setup(channel, GPIO.mode) , or optionaly for output
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.bool)
# to start at a specific value
# set board pin (see above) # 3 to input
GPIO.setup(3, GPIO.IN)
# set board pin #5 to output
GPIO.setup(5, GPIO.OUT)
# set board pin #7 to output w/ value of high
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH) # GPIO.LOW is also valid

# reading is as simple as GPIO.input(channel)
# this returns 0/GPIO.LOW/False or 1/GPIO.HIGH/True
print (GPIO.input(3))

# outputing is just as simple: GPIO.output(channel, state)
# the values you can output are the same as the ones you can input
GPIO.output(5,GPIO.LOW)

# both GPIO.setup and GPIO.output work with lists or tuples for channel
# inputs:
# chan_list = [11, 12, ...]
# chan_tupl = (13, 14, ...)
# GPIO.setup(chan_list, GPIO.OUT)
# GPIO.output(chan_tupl, (GPIO.HIGH, GPIO.LOW, ...))
# you can use a tuple as above to set each channel to a specific value

# clean up your toys after you are done with GPIO.cleanup() !
# this resets all channels that you have used to input w/ no
# pull up/down to avoid accidental shorts. This also resets your
# channel numbering scheme.
GPIO.cleanup()
# you can also clean up (a) specific channel(s) by passing in
# a channel, or a list or tuple of channels
# GPIO.cleanup(channel)
# GPIO.cleanup([channel_1, channel_2, ...])
# GPIO.cleanup((channel_3, channel_4, ...))

# find info about your RPi with
GPIO.RPI_INFO
# find RPi revision with
GPIO.RPI_INFO['P1_REVISION']
# get GPIO version with
GPIO.VERSION
