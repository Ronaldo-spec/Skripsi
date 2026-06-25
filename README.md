# Catfish Fry Size Classification using Computer Vision

Computer vision final project for classifying **catfish fry size categories** using CNN-based image classification and embedded deployment with **OpenMV Cam H7+**.

This repository is documented as a portfolio project to show applied machine learning, image classification, dataset preparation, model evaluation, and edge AI deployment.

---

## Project Overview

The project focuses on classifying catfish fry into size categories based on captured images. The goal is to support a more consistent and efficient size identification process compared with fully manual observation.

The model was developed using **MobileNetV2 transfer learning** with TensorFlow/Keras, converted into TensorFlow Lite format, and deployed through OpenMV IDE for embedded camera testing.

---

## Size Categories

| Class | Size Range |
|---|---|
| A | 1 - 3 cm |
| B | 4 - 5 cm |
| C | > 6 cm |

---

## Hardware Setup

| Component | Description |
|---|---|
| Camera | OpenMV Cam H7+ |
| Camera position | Approximately 20 cm above aquarium |
| Aquarium size | 20 cm x 15 cm |
| Water depth | Approximately 0.5 cm |
| Deployment tool | OpenMV IDE |

---

## Tech Stack

| Area | Technology |
|---|---|
| Machine Learning | TensorFlow, Keras |
| Model Architecture | MobileNetV2 transfer learning |
| Deployment Format | TensorFlow Lite `.tflite` |
| Embedded Vision | OpenMV Cam H7+ |
| Programming | Python |
| Evaluation | Accuracy, Precision, Recall, F1-score |

---

## Dataset Variants

Two dataset variants were used during experimentation:

| Dataset Variant | Total Images | Notes |
|---|---:|---|
| Fit | 630 | Earlier dataset configuration |
| Rectangle | 1,740 | Improved dataset configuration with stronger performance |

---

## Model Evaluation Summary

| Dataset Variant | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Fit | 64% | 0% | 47% | 0% |
| Rectangle | 89% | 87% | 83% | 82% |

The **Rectangle dataset** produced the strongest result and became the better-performing experiment in this project.

---

## Workflow

1. Capture catfish fry images using OpenMV camera setup.
2. Prepare image dataset based on size categories.
3. Train image classification model using MobileNetV2 transfer learning.
4. Evaluate model using classification metrics.
5. Convert trained model into TensorFlow Lite format.
6. Deploy and test the model using OpenMV IDE.

---

## Portfolio Notes

This project demonstrates:

- Computer vision problem formulation
- Image dataset preparation
- CNN / transfer learning implementation
- Model evaluation and comparison
- TensorFlow Lite deployment
- Embedded AI experimentation with OpenMV

---

## Future Improvements

- Increase dataset size and class balance.
- Improve image capture consistency.
- Add more lighting and water-condition variation.
- Test model robustness on unseen aquarium setups.
- Add deployment documentation and demo screenshots.

---

## Author

**Ronaldo Firmansyah**  
Programmer | Business Analyst | ERP/Application Support | SQL Reporting | Data Analyst

LinkedIn: [linkedin.com/in/ronaldofirmansyah](https://linkedin.com/in/ronaldofirmansyah)  
GitHub: [github.com/Ronaldo-spec](https://github.com/Ronaldo-spec)
