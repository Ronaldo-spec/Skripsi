import sensor
import image
import time
import tf
import pyb

# Inisialisasi kamera OpenMV
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
sensor.skip_frames(time=2000)  # Wait for sensor to adjust

# Inisialisasi model Keras
tfmodel = tf.load('titipan/tflite/RECT_coba2_BL00001_no-dropout.tflite', True)

# Threshold yang digunakan untuk find_blobs
thresholds = [(33, 100, 127, -30, -45, 52)]

# Get the class labels
class_labels = ['Grade A', 'Grade B', 'Grade C']

# Inisialisasi variabel untuk perhitungan jumlah bibit lele
total_bibit_lele = 0

# Loop utama
clock = time.clock()
while (True):
    clock.tick()

    img = sensor.snapshot()
    # Find blobs
    blobs = img.find_blobs(thresholds, invert=True)

    count_grade_a = 0
    count_grade_b = 0
    count_grade_c = 0

    for blob in blobs:
        square_size = max(blob.w(), blob.h())

        # Calculate the top-left corner coordinates of the square
        x = blob.cx() - square_size // 2
        y = blob.cy() - square_size // 2

        roi = [x,y,square_size, square_size]

        roi_img = img.copy(roi=roi)

        start_time = pyb.millis() # Waktu mulai klasifikasi

        for obj in tfmodel.classify(roi_img):
             # Get the predicted class label and confidence
             predicted_class = obj.output()
             max_result_value = max(predicted_class)
             most_likely_idx = predicted_class.index(max_result_value)

             # Get the predicted class label
             predicted_label = class_labels[most_likely_idx]

             # Get the confidence score
             confidence_score = max_result_value

             # Update counts based on the predicted class
             if most_likely_idx == 0:
                if max_result_value >= 0.5:
                    count_grade_a =+ 1
             elif most_likely_idx == 1:
                if max_result_value >= 0.5:
                    count_grade_b =+ 1
             elif most_likely_idx == 2:
                if max_result_value >= 0.5:
                    count_grade_c =+ 1

             print("****************")
             # Print the predicted class label and confidence score
             print("Predicted Label: %s" % predicted_label)
             print("Confidence Score: %.2f" % confidence_score)

             # Print the predicted class label and confidence score on the image
             label_str = "%s: %.2f" % (predicted_label, confidence_score)
             img.draw_string(blob.x(),blob.y(), label_str, color=(0, 0, 0), scale=1)


        end_time = pyb.millis() # Waktu akhir klasifikasi
        classification_time = end_time - start_time # Waktu klasifikasi dalam milidetik
        img.draw_rectangle((x, y, square_size,square_size), color=(0, 255, 0))
        img.draw_cross(blob.cx(), blob.cy(), color=(0, 255, 0))

    # Calculate total number of fish seeds
    total_bibit_lele = count_grade_a + count_grade_b + count_grade_c

    # Print results
    print("Grade A: %d" % count_grade_a)
    print("Grade B: %d" % count_grade_b)
    print("Grade C: %d" % count_grade_c)

    img.draw_string(10, 10, "A: %d" % count_grade_a, color = (70, 80, 90), scale = 1)
    img.draw_string(10, 10, "B: %d" % count_grade_b, color = (70, 80, 90), scale = 1)
    img.draw_string(10, 10, "C: %d" % count_grade_c, color = (70, 80, 90), scale = 1)
    img.draw_string(40, 40, "C: %d" % count_grade_c, color = (70, 80, 90), scale = 1)
    # Print total results
    print("Total Bibit Lele: %d" % total_bibit_lele)

    # Print FPS
    print(clock.fps())
