# Research Context

This document summarizes the academic research context behind the catfish fry size classification project.

## Thesis Title

**Towards Automatic Catfish Fry Grading: Catfish Fry Size Classification Using Convolutional Neural Network (CNN) with OpenMV Cam**

## Background

Catfish fry grading is commonly performed by farmers to separate fry based on size. The process is important because catfish fry can grow at different rates and larger fry may cannibalize smaller fry. Manual grading can produce inconsistent results, especially when fry do not match the sorting container hole size accurately.

The research explores the use of deep learning and computer vision to support a more consistent grading process.

## Research Objective

The main objective is to apply a CNN-based image classification approach to classify catfish fry grades automatically using OpenMV Cam H7+.

## Method Summary

- Capture catfish fry image data using OpenMV Cam H7+.
- Prepare image dataset for three class categories: Grade A, Grade B, and Grade C.
- Train image classification models using CNN with MobileNetV2 transfer learning.
- Compare dataset variants based on image size and blob extraction method.
- Convert the trained model into TensorFlow Lite format.
- Test the model using static image testing and real-time testing on OpenMV.

## Experimental Materials

The research compared four experimental dataset configurations:

| Configuration | Description |
|---|---|
| 96 x 96 blobs.fit | Image size 96 x 96 using blobs.fit |
| 96 x 96 blobs.rect | Image size 96 x 96 using blobs.rect |
| 128 x 128 blobs.fit | Image size 128 x 128 using blobs.fit |
| 128 x 128 blobs.rect | Image size 128 x 128 using blobs.rect |

## Hardware and Environment

| Component | Description |
|---|---|
| Camera | OpenMV Cam H7+ |
| Deployment | OpenMV IDE |
| Aquarium size | 20 cm x 15 cm x 15 cm |
| Water depth | Approximately 0.5 cm |
| Camera position | Approximately 20 cm above aquarium |

## Best Performing Result

The best-performing experiment was obtained from the **128 x 128 blobs.rect** configuration.

| Test Type | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Static image testing | 80% | 70% | 70% | 68% |
| Real-time testing | 89% | 87% | 83% | 82% |

## Key Takeaways

- CNN with MobileNetV2 can be applied to classify catfish fry grades.
- The `blobs.rect` approach performed better than `blobs.fit` in this research.
- The 128 x 128 image configuration produced stronger results than the 96 x 96 configuration.
- OpenMV Cam H7+ can support lightweight embedded vision testing with TensorFlow Lite.

## Portfolio Notes

This repository should be reviewed as an applied computer vision and edge AI project. The most relevant aspects for portfolio review are:

- Problem formulation in aquaculture / fish farming context.
- Dataset preparation and preprocessing.
- CNN transfer learning using MobileNetV2.
- Model comparison and evaluation.
- TensorFlow Lite conversion.
- Embedded deployment using OpenMV.

## Privacy and Repository Scope

The full thesis report is not stored directly in this repository because it may contain academic approval pages, signatures, and other formal personal information. This summary keeps the technical research context available while keeping the repository clean and portfolio-oriented.
