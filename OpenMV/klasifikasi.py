import sensor
import image
import time
import tf
import pyb

# Inisialisasi kamera OpenMV
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)  # Wait for sensor to adjust

# Inisialisasi model Keras
#tfmodel = tf.load('lele_model/ronaldo/modelku-fit_data-baru_88.tflite', True)
tfmodel = tf.load('lele_model/ronaldo/modelku-fit_coba2_85.tflite', True)

# Threshold yang digunakan untuk find_blobs
thresholds = [(43, 100, -100, 60, -50, 85)]

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
    blobs = img.find_blobs(thresholds, invert=True, merge=True)

    # Inisialisasi variabel perhitungan kelas
    count_grade_a = 0
    count_grade_b = 0
    count_grade_c = 0

    for blob in blobs:
        # Only save the part of the image inside the bounding rectangle
        roi = blob.rect()

        roi_img = img.copy(roi=roi)

        pyb.delay(1000) #delay untuk menangkap gambar

        for obj in tfmodel.classify(roi_img, min_scale=1.0, scale_mul=0.5, x_overlap=0.0, y_overlap=0.0):
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
               if max_result_value > 0.05:
                  count_grade_a =+ 1
            elif most_likely_idx == 1:
               if max_result_value > 0.05:
                  count_grade_b =+ 1
            elif most_likely_idx == 2:
               if max_result_value > 0.05:
                  count_grade_c =+ 1

            print("****************")
            # Print the predicted class label and confidence score
            print("Predicted Label: %s" % predicted_label)
            print("Confidence Score: %.2f" % confidence_score)


        # Draw a rectangle and a cross on the original image
        #img.draw_rectangle(x, y, 96, 96, color = (255, 0, 0))
        #img.draw_rectangle(x, y, 100, 100, color = (255, 0, 0))
        img.draw_rectangle(blob.rect(), color=(0, 255, 0))
        img.draw_cross(blob.cx(), blob.cy(), color=(0, 255, 0))

    # Calculate total number of fish seeds
    total_bibit_lele = count_grade_a + count_grade_b + count_grade_c

    # Print results for each object
    for i, blob in enumerate(blobs):
        print("Object %d:" % (i+1))
        print("Grade A: %d" % count_grade_a)
        print("Grade B: %d" % count_grade_b)
        print("Grade C: %d" % count_grade_c)

    # Print total results
    print("Total Bibit Lele: %d" % total_bibit_lele)

    # Print FPS
    print(clock.fps())
