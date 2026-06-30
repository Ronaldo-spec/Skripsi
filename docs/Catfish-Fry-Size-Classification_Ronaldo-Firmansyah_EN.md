# Catfish Fry Size Classification Using CNN and OpenMV Cam

**English Portfolio Report**  
Prepared by **Ronaldo Firmansyah**  
Informatics Engineering - State Polytechnic of Malang, 2023

---

## Executive Summary

This report presents an English portfolio version of a final thesis project titled **Towards Automatic Catfish Fry Grading: Catfish Fry Size Classification Using Convolutional Neural Network (CNN) with OpenMV Cam**.

The project explored the use of computer vision and deep learning to classify catfish fry into size categories automatically. It used CNN-based image classification with **MobileNetV2 transfer learning**, **TensorFlow/Keras**, **TensorFlow Lite**, and **OpenMV Cam H7+** deployment.

The strongest configuration was **128 x 128 blobs.rect**, which achieved **89% accuracy**, **87% precision**, **83% recall**, and **82% F1-score** in real-time testing.

---

## Problem Background

Catfish fry grading is an important process in catfish farming. Fry can grow at different rates even when they are of similar age. If fry with different sizes are mixed, smaller fry can be affected by cannibalism and buyers may receive fry that do not match the intended size category.

Traditional grading commonly uses manual sorting tools such as perforated containers or grading trays. However, manual grading can still produce inconsistent results when fry that do not match the target size pass through the sorting holes.

This project addressed the problem by applying computer vision and CNN-based classification to support a more consistent and automated grading process.

---

## Research Objective

The main objective was to apply deep learning with CNN to classify catfish fry sizes automatically using images captured through an OpenMV-based workflow.

The project aimed to:

- Apply CNN to the catfish fry grading problem.
- Classify catfish fry into predefined grade categories.
- Evaluate model performance through static image testing and real-time OpenMV testing.
- Identify the best image configuration for the grading task.

---

## Size Classes

| Class | Size Range |
|---|---|
| Grade A | 1 - 3 cm |
| Grade B | 4 - 5 cm |
| Grade C | > 6 cm |

---

## Hardware and Software Setup

| Area | Technology / Component |
|---|---|
| Camera | OpenMV Cam H7+ |
| Camera position | Approximately 20 cm above the aquarium |
| Aquarium size | 20 cm x 15 cm x 15 cm |
| Water depth | Approximately 0.5 cm |
| Model architecture | MobileNetV2 transfer learning |
| Training framework | TensorFlow / Keras |
| Deployment format | TensorFlow Lite (.tflite) |
| Deployment tool | OpenMV IDE |

---

## Methodology

The workflow combined dataset collection, image preprocessing, model training, model conversion, and embedded testing.

1. Capture catfish fry videos/images using the OpenMV camera setup.
2. Extract image frames and prepare dataset folders by grade category.
3. Preprocess images using different image sizes and blob formats.
4. Train the model using MobileNetV2 transfer learning.
5. Evaluate the model using classification metrics.
6. Convert the trained model into TensorFlow Lite format.
7. Test the model using static images and real-time OpenMV inference.

---

## Dataset and Experimental Configurations

The research compared multiple image configurations to understand which preprocessing and image format provided stronger model performance.

| Configuration | Description |
|---|---|
| 96 x 96 blobs.fit | Image size 96 x 96 using blobs.fit |
| 96 x 96 blobs.rect | Image size 96 x 96 using blobs.rect |
| 128 x 128 blobs.fit | Image size 128 x 128 using blobs.fit |
| 128 x 128 blobs.rect | Image size 128 x 128 using blobs.rect |

| Dataset Variant | Total Images | Notes |
|---|---:|---|
| Fit | 630 | Earlier dataset configuration |
| Rectangle | 1,740 | Improved dataset configuration with stronger performance |

---

## Evaluation Metrics

The model was evaluated using confusion matrix representation and common classification metrics:

- Accuracy
- Precision
- Recall
- F1-score

Static image testing evaluated the trained model on image samples, while real-time testing validated the OpenMV-based workflow.

---

## Results

The best-performing configuration was **128 x 128 blobs.rect**. It performed better than blobs.fit in both static image testing and real-time testing.

| Test Type | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Static image testing - 128 x 128 blobs.rect | 80% | 70% | 70% | 68% |
| Real-time testing - 128 x 128 blobs.rect | 89% | 87% | 83% | 82% |

The real-time result is the strongest portfolio highlight because it demonstrates that the model was tested in an embedded camera workflow, not only in offline static image evaluation.

---

## Portfolio Value

This project is a strong portfolio item because it combines original research, applied machine learning, computer vision, embedded deployment, and formal academic reporting.

It demonstrates:

- Computer vision problem formulation in an agriculture/aquaculture context.
- CNN and transfer learning implementation using MobileNetV2.
- Image dataset preparation and preprocessing comparison.
- Model evaluation using accuracy, precision, recall, F1-score, and confusion matrix.
- TensorFlow Lite conversion and embedded testing through OpenMV Cam H7+.
- Formal thesis documentation and measurable experimental results.

---

## Limitations and Future Improvements

The research was conducted within a controlled experimental setup. Future development can improve robustness by expanding the dataset, increasing variation in lighting and water conditions, testing different camera positions, and validating the model across more farms or aquarium environments.

Recommended improvements:

- Increase dataset size and improve class balance.
- Capture more variation in lighting, water clarity, fish movement, and aquarium conditions.
- Improve real-time counting logic and object isolation.
- Test the model on unseen locations and real farm conditions.
- Explore newer lightweight model architectures for embedded deployment.

---

## Closing

The project demonstrates that CNN-based computer vision can be applied to catfish fry grading using MobileNetV2 and OpenMV Cam H7+. The **128 x 128 blobs.rect** configuration produced the strongest result and became the most suitable configuration for portfolio presentation.

As a portfolio artifact, this project supports professional positioning in computer vision, machine learning, Python, data preprocessing, embedded AI experimentation, and technical documentation.
