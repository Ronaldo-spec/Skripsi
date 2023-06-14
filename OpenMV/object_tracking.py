
import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time

sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
#sensor.set_vflip(True) # Flips the image vertically
#sensor.set_hmirror(True) # Mirrors the image horizontally
sensor.skip_frames(time = 2000) # Skip some frames to let the image stabilize
sensor.set_framerate(40)

# Define the min/max LAB values we're looking for
thresholds = (41, 100, 80, -40, -60, 20)
record_time = 60000 # 10 seconds in milliseconds

clock = time.clock() # Instantiates a clock object

start = pyb.millis()
while True : #pyb.elapsed_millis(start) < record_time:
    clock.tick() # Advances the clock
    img = sensor.snapshot() # Takes a snapshot and saves it in memory

    # Overlapping blobs will be merged
    blobs = img.find_blobs([thresholds], invert=True, merge=True)

    # Draw blobs
    for blob in blobs:
        roi = blob.rect()
        #imgroi = img.copy(roi=roi)
        # Draw a rectangle where the blob was found
        img.draw_rectangle(blob.rect(), color=(0,255,0))
        # Draw a cross in the middle of the blob
        img.draw_cross(blob.cx(), blob.cy(), color=(0,255,0))
        #filename = "imageC_" + str(pyb.millis()) + ".bmp"
        #imgroi.save("image/test-asus/gradeC/" + filename)


    print(clock.fps()) # Prints the framerate to the serial console
