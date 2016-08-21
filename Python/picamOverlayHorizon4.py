import time
import picamera
import numpy as np
import skimage.draw as skd

# Create an array representing a 1280x720 image of
# a cross through the center of the display. The shape of
# the array must be of the form (height, width, color)
height = 720
width = 1280
a = np.zeros((height, width, 3), dtype=np.uint8)
y = 357
rr, cc = skd.line(y,0, y, width-1)
a[rr, cc, :] = 0xff

dy = 1

with picamera.PiCamera() as camera:
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (width, height)
    camera.framerate = 24
    minPeriod = 1.0 / camera.framerate
    
    camera.start_preview()
    
    # Add the overlay directly into layer 3 with transparency;
    # we can omit the size parameter of add_overlay as the
    # size is the same as the camera's resolution
    la = camera.add_overlay(a.data, layer=3, alpha=64)
    lastUpdateTime = time.time()  
    try:
        # Wait indefinitely until the user terminates the script
        while True:
            a[rr, cc, :] = 0x00
            if (y >= 700) or (y <= 20):
                dy = -dy
            y = y + dy
            rr, cc = skd.line(y,0, y, width-1)
            a[rr, cc, :] = 0xff
            if ((time.time() - lastUpdateTime) > minPeriod):
                la.update(a.data)
                lastUpdateTime = time.time()
            
    finally:
        camera.remove_overlay(la)
