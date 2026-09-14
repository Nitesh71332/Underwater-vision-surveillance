# Underwater Vision-Based Surveillance

Internship project focused on underwater image enhancement and object detection using Machine Learning and Artificial Intelligence.

## Datasets

- well.v8i.yolov8 — 4 classes
- DIATAquarium.v4i.yolov8 — 11 classes
- Aquatic Plant.v2i.yolov8 — 1 class

All three datasets are evaluated separately.

## Project Pipeline

Underwater Images → Data Inspection → Data Preparation → Preprocessing → Image Enhancement → YOLO Object Detection → Evaluation

## Candidate Methods

- Enhancement: White Balance, CLAHE, Water-Net, FUnIE-GAN
- Detection: YOLO-based transfer learning
- Tracking: Only if video data is available

## Evaluation

- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95
- PSNR / SSIM / UIQM where applicable
- Inference / processing time

## Progress

- Day 1 — Problem Understanding
- Day 2 — Literature Review
- Day 3 — Research Framing & Mentor Review
- Day 4 — Dataset Schema & Risk Checklist
- Day 5 — Experiment Plan & Pipeline
- Day 6 — Methodology V1
- Day 7 — Initial Dataset Inspection & Preliminary Dataset Report
- Day 8 — Dataset & Annotation Quality Report
- Day 9 — Data Preparation Progress Pack
- Day 10 — Visual Exploratory Data Analysis (EDA)
- Day 11 — Dataset V1 Preparation
- Day 12 — Dataset V1 Review & Finalization
- Day 13 — Image Enhancement & Detection Preparation
- Day 14 — Peer Visual Review & Experiment Hypotheses

## Current Status

- Dataset inspection completed for all three datasets
- Dataset and annotation quality audits completed
- Visual EDA completed
- Dataset V1 prepared with 640 × 640 image size, RGB format and 0–1 normalization
- Training augmentation strategy defined
- Source-level leakage risks identified and documented
- White Balance + CLAHE enhancement baseline implemented
- 13,808 training images enhanced across all three datasets
- Original and enhanced datasets maintained separately
- YOLO configuration prepared for enhanced training data
- Original vs Enhanced YOLO experiment defined
- Experiment hypotheses and evaluation metrics finalized
- No video data is currently available, so tracking is not included in the current implementation

## Next Step

- YOLO model training
- Compare Original vs Enhanced images
- Evaluate Precision, Recall, mAP@0.5, mAP@0.5:0.95 and inference time
- Analyse the effect of image enhancement on detection performance

**Author:** C. Nitesh Kumar
