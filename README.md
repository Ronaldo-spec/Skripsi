# Catfish Fry Size Classification using CNN and OpenMV

Computer vision final project for classifying **catfish fry size categories** using CNN-based image classification and embedded deployment with **OpenMV Cam H7+**.

This repository is documented as a portfolio project to show original research, applied machine learning, image classification, dataset preparation, model evaluation, TensorFlow Lite conversion, and edge AI deployment.

---

## Project Overview

The project focuses on classifying catfish fry into size categories based on captured images. The goal is to support a more consistent and efficient size identification process compared with fully manual grading.

The model was developed using **MobileNetV2 transfer learning** with TensorFlow/Keras, converted into TensorFlow Lite format, and deployed through OpenMV IDE for embedded camera testing.

For a more detailed research summary, see:

[Research Context](docs/research_context.md)

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
| Aquarium size | 20 cm x 15 cm x 15 cm |
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
| Evaluation | Accuracy, Precision, Recall, F1-score, Confusion Matrix |

---

## Experimental Configurations

Four experimental configurations were compared during model development:

| Configuration | Description |
|---|---|
| 96 x 96 blobs.fit | Image size 96 x 96 using blobs.fit |
| 96 x 96 blobs.rect | Image size 96 x 96 using blobs.rect |
| 128 x 128 blobs.fit | Image size 128 x 128 using blobs.fit |
| 128 x 128 blobs.rect | Image size 128 x 128 using blobs.rect |

---

## Dataset Variants

Two dataset variants were used during experimentation:

| Dataset Variant | Total Images | Notes |
|---|---:|---|
| Fit | 630 | Earlier dataset configuration |
| Rectangle | 1,740 | Improved dataset configuration with stronger performance |

---

## Model Evaluation Summary

The strongest configuration was **128 x 128 blobs.rect**.

| Test Type | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Static image testing | 80% | 70% | 70% | 68% |
| Real-time testing | 89% | 87% | 83% | 82% |

The real-time testing result became the strongest portfolio highlight because it demonstrates that the model could be tested through the OpenMV-based workflow, not only through static image evaluation.

---

## Reports

| Report | Description |
|---|---|
| [Indonesian Thesis Report - Secured PDF](docs/Catfish-Fry-Size-Classification_Ronaldo-Firmansyah_ID.pdf) | Original Indonesian thesis report in secured PDF format. |
| [English Portfolio Report - Markdown](docs/Catfish-Fry-Size-Classification_Ronaldo-Firmansyah_EN.md) | English portfolio version rewritten for GitHub and LinkedIn review. |
| [English Portfolio Report - Secured PDF](docs/Catfish-Fry-Size-Classification_Ronaldo-Firmansyah_EN.pdf) | English secured PDF version for portfolio distribution. |
| [Report Security Note](docs/report_security_note.md) | Notes about PDF security limitations and repository scope. |

---

## Workflow

1. Capture catfish fry images using OpenMV camera setup.
2. Prepare image dataset based on size categories.
3. Train image classification model using MobileNetV2 transfer learning.
4. Evaluate model using classification metrics and confusion matrix.
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
- Formal academic report writing

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
