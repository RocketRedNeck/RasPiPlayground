import picamera as piC
import time

cam = piC.PiCamera()

cam.hflip = True
cam.vflip = True

try:
    cam.resolution = (640,480)
    cam.start_preview()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    cam.stop_preview()
    cam.close()
