# Untitled - By: HOSNOL ARIFIN - Mon Jun 26 2023

import image, tf, os

# Get the class labels
class_labels = ['Grade A', 'Grade B', 'Grade C']

# Inisialisasi model Keras
tfmodel = tf.load('titipan/tflite/FIT_coba3_BL00001_no-dropout_size96.tflite', True)

image_dir = "titipan/fit/testing/gradeC"

#img = image.Image("image/testing rect/grade A/A (252).bmp")

# Initialize counters for each grade
grade_counts = [0, 0, 0]

# Loop melalui setiap gambar dalam direktori
for filename in os.listdir(image_dir):
    img = image.Image("titipan/fit/testing/gradeC/"+filename)
    for obj in tfmodel.classify(img):
        # Get the predicted class label and confidence
        predicted_class = obj.output()
        max_result_value = max(predicted_class)
        most_likely_idx = predicted_class.index(max_result_value)

        # Get the predicted class label
        predicted_label = class_labels[most_likely_idx]

        # Get the confidence score
        confidence_score = max_result_value

        # Increment the counter for the predicted grade
        grade_counts[most_likely_idx] += 1

        # Print the predicted class label and confidence score
        print("--------------------------")
        print(filename)
        print("Predicted Label: %s" % predicted_label)
        print("Confidence Score: %.2f" % confidence_score)

# Calculate and print the percentage for each grade
total_count = sum(grade_counts)
print("\nGrade Classification Summary:")
for i, grade_count in enumerate(grade_counts):
    grade_name = class_labels[i]
    percentage = (grade_count / total_count) * 100
    print("%s: %.2f%%" % (grade_name, percentage))
