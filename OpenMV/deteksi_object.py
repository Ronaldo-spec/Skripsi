# Untitled - By: HOSNOL ARIFIN - Mon Mar 13 2023

import sensor, image, time

# Sensor settings
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px


# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
fish_cascade = image.HaarCascade("/haarcascades/fish_cascade.cascade", stages=25)
print(fish_cascade)

# FPS clock
clock = time.clock()
thresholds = (36, 100, -99, 42, -68, 23)

while(True):
    clock.tick()
    ## Gamma, contrast, and brightness correction are applied to each color channel. The
    ## values are scaled to the range per color channel per image type...
    img = sensor.snapshot()



    # Find objects.
    # Note: Lower scale factor scales-down the image more and detects smaller objects.
    # Higher threshold results in a higher detection rate, with more false positives.
    objects = img.find_features(fish_cascade, threshold=0.90, scale_factor=1.25)

    # Draw objects
    for r in objects:
        img.draw_rectangle(r, color=(255,0,0))

    # Print FPS.
    print(clock.fps())
