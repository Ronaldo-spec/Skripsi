# Untitled - By: HOSNOL ARIFIN - Mon Mar 27 2023

import sensor, image, pyb, time, os

record_time = 10000 # 10 seconds in milliseconds

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.CIF)
sensor.skip_frames(time = 2000)
clock = time.clock()

stream = image.ImageIO("/GRADECGray.bin", "w")

start = pyb.millis()

grayscale_thres = (200, 255)

while pyb.elapsed_millis(start) < record_time:
    clock.tick()
    img = sensor.snapshot().gamma_corr(gamma = 5, contrast = 1.0, brightness = 0.0)

    for i in range(20):
        img.binary([grayscale_thres])
        img.dilate(0)

    # Modify the image if you feel like here...
    stream.write(img)
    filename = "imageC_" + str(pyb.millis()) + ".PNG"
    img.save("image/Grade C/" + filename)
    print(clock.fps())
