# Underwater Vision-Based Surveillance

Internship project focused on underwater image enhancement and object detection using Machine Learning and Artificial Intelligence.

## Datasets

- well.v8i.yolov8 — 4 classes
- DIATAquarium.v4i.yolov8 — 11 classes
- Aquatic Plant.v2i.yolov8 — 1 class

All three datasets are evaluated separately.

## Project Pipeline

Underwater Images → Data Inspection → Data Preparation → Preprocessing → Image Enhancement → YOLO Object Detection → Evaluation → Comparison

## Methods

- Enhancement: White Balance + CLAHE
- Detection: YOLOv8n with transfer learning
- Baseline: Original Image + YOLOv8n
- Enhanced Pipeline: White Balance + CLAHE + YOLOv8n
- Tracking: Not included because no video data is currently available
- Water-Net and FUnIE-GAN: Reviewed as candidate methods but not implemented

## Preprocessing

- Image size: 640 × 640
- Color format: RGB
- Pixel normalization: 0–1
- Training augmentation: Horizontal flip, small rotation, scale variation and brightness/contrast variation
- Validation and test data were not augmented
- Original raw datasets were preserved separately

## Evaluation

- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95
- Inference time / FPS
- PSNR / SSIM / UIQM were considered where applicable, but no quantitative project-dataset values were reported

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
- Day 15 — Enhancement Baseline Quantitative Analysis
- Day 16 — Original YOLOv8n Baseline Training
- Day 17 — Enhanced YOLOv8n Training
- Day 18 — Baseline vs Enhanced Analysis
- Day 19 — Hyperparameter Tuning
- Day 20 — Robustness & Ablation Analysis
- Day 21 — Best Candidate Review
- Day 22 — Final Model & Pipeline Freeze

## Current Status

- Dataset inspection completed for all three datasets
- Dataset and annotation quality audits completed
- Visual EDA completed
- Dataset V1 prepared with 640 × 640 image size, RGB format and 0–1 normalization
- Training augmentation strategy defined
- Source-level leakage risks identified and documented
- White Balance + CLAHE enhancement implemented
- Original and enhanced datasets maintained separately
- Original YOLOv8n baseline trained on all three datasets
- Enhanced YOLOv8n trained on all three datasets
- Hyperparameter tuning completed for Aquatic Plant and Well
- Best validation configurations selected
- Robustness and ablation analysis completed
- Final model configurations frozen
- Final model checkpoints saved and verified
- No video data is currently available, so tracking is not included in the current implementation

## Final Model Configurations

### DIATAquarium

- Pipeline: Original Image + YOLOv8n
- Precision: 90.02%
- Recall: 92.09%
- mAP@0.5: 92.72%
- mAP@0.5:0.95: 65.90%

### Aquatic Plant

- Pipeline: Original Image + White Balance + CLAHE + YOLOv8n
- Learning Rate: 0.0005
- Batch Size: 32
- Epochs: 30
- Precision: 95.4%
- Recall: 96.1%
- mAP@0.5: 98.5%
- mAP@0.5:0.95: 71.5%

### Well

- Pipeline: Original Image + White Balance + CLAHE + YOLOv8n
- Learning Rate: 0.001
- Batch Size: 16
- Epochs: 30
- Precision: 35.7%
- Recall: 40.1%
- mAP@0.5: 36.8%
- mAP@0.5:0.95: 16.8%

## Key Findings

White Balance + CLAHE did not consistently improve YOLOv8n detection across all three datasets. Its effect was dataset-dependent.

- Aquatic Plant showed improvement in Recall and mAP@0.5.
- DIATAquarium showed decreased detection performance with WB+CLAHE.
- Well showed small Precision and Recall improvements but a decrease in mAP compared with the original baseline.
- Dataset imbalance and source-level overlap remain important limitations.
- The local DIATAquarium copy does not contain a separate test set, so its final evaluation is based on validation results.
- Aquatic Plant and Well were selected for further tuning based on validation performance.
- Original YOLOv8n was retained as the baseline reference.

## Final Project Scope

The final implementation focuses on:

**Underwater Image Enhancement → YOLOv8n Object Detection → Performance Comparison**

All three supplied datasets are evaluated separately.

Tracking is outside the current implementation scope because video data is not available.

## Final Artifacts

The final project includes:

- Final model checkpoints
- Frozen configuration file
- Final model summary
- Dataset preparation and preprocessing documentation
- Enhancement implementation
- YOLOv8n training and evaluation results
- Comparison and analysis
- Day-wise internship documentation

## Next Step

- Final report preparation
- Final results presentation
- Documentation of limitations and future improvements
- Final project submission

**Author:** C. Nitesh Kumar
