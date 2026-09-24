# Underwater Vision-Based Surveillance Using Machine Learning and Artificial Intelligence

## 1. Project Overview

This project investigates underwater object detection using Machine Learning and Artificial Intelligence. The study evaluates three supplied underwater datasets separately and examines whether classical underwater image enhancement affects YOLOv8n object detection performance.

The implemented project pipeline is:

Underwater Image → Quality Check → Preprocessing → Image Enhancement → YOLOv8n Detection → Evaluation → Error Analysis

## 2. Datasets

Three supplied datasets were used:

### DIATAquarium
- 11 object classes
- Original images were used with YOLOv8n for the final configuration.

### Aquatic Plant
- 1 object class
- Final configuration: White Balance + CLAHE + YOLOv8n.

### Well
- 4 object classes
- Final configuration: White Balance + CLAHE + YOLOv8n.

All three datasets were evaluated separately.

## 3. Preprocessing

The finalized preprocessing configuration was:

- Image size: 640 × 640
- Color format: RGB
- Pixel normalization: 0–1
- Raw dataset: preserved
- Training augmentation: applied only during training where used.

The preprocessing implementation is available in:

`preprocessing/preprocessing.py`

## 4. Image Enhancement

The implemented classical enhancement method combines:

Original Image → White Balance → CLAHE → Enhanced Image

### White Balance

White Balance reduces underwater colour distortion and colour cast.

### CLAHE

CLAHE stands for Contrast Limited Adaptive Histogram Equalization. It improves local image contrast while limiting excessive contrast amplification.

The implementation is available in:

`enhancement/wb_clahe.py`

## 5. Object Detection

YOLOv8n was used as the object detector.

The detector produces:

- Object class
- Bounding box
- Confidence score

The inference implementation is available in:

`detection/inference.py`

## 6. Final Model Configurations

### DIATAquarium

Configuration:

Original Image → YOLOv8n

Validation:
- Precision: 90.02%
- Recall: 92.09%
- mAP@0.5: 92.73%
- mAP@0.5:0.95: 65.92%

### Aquatic Plant

Configuration:

Original Image → White Balance + CLAHE → YOLOv8n

Final H03 configuration:
- Learning rate: 0.0005
- Batch size: 32
- Epochs: 30
- Image size: 640 × 640
- Optimizer: AdamW

Validation:
- Precision: 95.4%
- Recall: 96.1%
- mAP@0.5: 98.5%
- mAP@0.5:0.95: 71.5%

Test:
- Precision: 97.99%
- Recall: 90.26%
- mAP@0.5: 96.75%
- mAP@0.5:0.95: 71.12%

### Well

Configuration:

Original Image → White Balance + CLAHE → YOLOv8n

Final H04 configuration:
- Learning rate: 0.001
- Batch size: 16
- Epochs: 30
- Image size: 640 × 640
- Optimizer: AdamW

Validation:
- Precision: 35.7%
- Recall: 40.1%
- mAP@0.5: 36.8%
- mAP@0.5:0.95: 16.8%

Test:
- Precision: 43.00%
- Recall: 37.46%
- mAP@0.5: 39.34%
- mAP@0.5:0.95: 16.15%

## 7. Evaluation Metrics

The project uses:

- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95
- Inference time
- Model size

The evaluation implementation is available in:

`evaluation/evaluate.py`

## 8. Runtime and Model Size

The final models are approximately 5.95–5.96 MB.

Measured inference speeds:

- DIAT: 45.16 FPS
- Aquatic Plant: 102.02 FPS
- Well: 100.21 FPS

The reported inference time measures YOLO inference and excludes separate White Balance + CLAHE preprocessing time.

## 9. Error Analysis

Representative error-analysis images are stored in:

`figures/error_analysis/`

Observed failure conditions included:

- Haze and low underwater visibility
- Small objects
- Objects near image boundaries
- Visually similar classes
- Low-confidence predictions
- Class imbalance

DIAT showed Fish/Fishes confusion.

Aquatic Plant showed missed and low-confidence plant detections.

Well showed difficulties with fishes and stone objects.

## 10. Training and Prediction Figures

Training figures are stored in:

`figures/training/`

Representative prediction images are stored in:

`figures/predictions/`

These figures provide visual evidence of model training, predictions and failure cases.

## 11. Final Model Files

The final trained model checkpoints are stored in:

`models/DIAT_Baseline/best.pt`

`models/Aquatic_Plant_H03/best.pt`

`models/Well_H04/best.pt`

## 12. Limitations

- The local DIAT dataset copy did not contain a separate test set, so the available validation set was used for final reported DIAT evaluation.
- Source overlap was identified in the supplied datasets.
- Well has strong class imbalance, particularly for rare classes.
- Enhancement effects were dataset- and class-dependent.
- The exact cause of an individual detection failure cannot be confirmed from visual inspection alone.
- Error analysis examined representative difficult cases rather than every prediction.
- Water-Net and FUnIE-GAN were reviewed as literature candidates but were not implemented in the final pipeline.
- Tracking was excluded because video data was not available in the current project scope.

## 13. Reproducibility

The repository contains the preprocessing, enhancement, detection and evaluation code together with final result tables and representative figures.

Required Python packages are listed in:

`requirements.txt`

Final model checkpoints are stored separately under the `models/` directory.

## 14. Project Conclusion

The project demonstrates an end-to-end underwater object detection workflow using YOLOv8n and classical image enhancement.

The experiments show that White Balance + CLAHE does not produce a uniform improvement across all datasets. Its effect depends on the dataset and object classes.

The final results, model checkpoints, representative predictions and error-analysis images are included as project artifacts.
