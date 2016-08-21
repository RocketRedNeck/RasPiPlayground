import picamera as piC
import time

cam = piC.PiCamera()

cam.hflip = True
cam.vflip = True

try:
    cam.resolution = (1920,1080)
    cam.start_preview()
    cam.annotate_text = 'hello'
    t = 0
    while True:
        time.sleep(1)
        t += 1
        cam.annotate_text = ("Time since start:\n" + str(t))
        
except KeyboardInterrupt:
    cam.stop_preview()
    cam.close()
