# Untitled - By: HOSNOL ARIFIN - Mon Mar 27 2023

import sensor, image, pyb, time, os

record_time = 10000 # 10 seconds in milliseconds

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.CIF)
sensor.skip_frames(time = 2000)
clock = time.clock()

# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
fish_cascade = image.HaarCascade("/haarcascades/fish_cascade.cascade", stages=25)
print(fish_cascade)

stream = image.ImageIO("/GRADEB_ori_kotak2.bin", "w")

# Red LED on means we are capturing frames.
pyb.LED(1).on()

start = pyb.millis()
while pyb.elapsed_millis(start) < record_time:
    clock.tick()
    img = sensor.snapshot()
    # Find objects.
    # Note: Lower scale factor scales-down the image more and detects smaller objects.
    # Higher threshold results in a higher detection rate, with more false positives.
    objects = img.find_features(fish_cascade, threshold=0.90, scale_factor=1.25)

    # Draw objects
    for r in objects:
        img.draw_rectangle(r, color=(255,0,0))

    # Modify the image if you feel like here...
    stream.write(img)
    filename = "imageB_" + str(pyb.millis()) + ".PNG"
    img.save("image/Grade B_Backup/" + filename)
    print(clock.fps())
