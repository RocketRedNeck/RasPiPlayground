import time
import picamera
import numpy as np

# Create an array representing a 1280x720 image of
# a cross through the center of the display. The shape of
# the array must be of the form (height, width, color)
a = np.zeros((720, 1280, 3), dtype=np.uint8)
a[357:363, 620:660, :] = 0xff
a[340:380, 637:643, :] = 0xff

# empty overlay for keeping alpha apparently constant when
# blinking
b = np.zeros((720, 1280, 3), dtype=np.uint8)

with picamera.PiCamera() as camera:
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()
    # Add the overlay directly into layer 3 with transparency;
    # we can omit the size parameter of add_overlay as the
    # size is the same as the camera's resolution
    la = camera.add_overlay(a.data, layer=3, alpha=64)
    lb = camera.add_overlay(b.data, layer=4, alpha=0)
    try:
        # Wait indefinitely until the user terminates the script
        while True:
            time.sleep(0.5)
            la.alpha = 0;
            lb.alpha = 64
            time.sleep(0.5)
            la.alpha = 64;
            lb.alpha = 0
    finally:
        camera.remove_overlay(la)
        camera.remove_overlay(lb)
