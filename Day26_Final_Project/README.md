# Day 26 — Final Software Package & Documentation

## Objective

Day 26 focused on preparing the final software package,documentation,results,figures and reproducibility files for the Underwater Vision-Based Surveillance project.

The final package contains the preprocessing,underwater image enhancement,YOLOv8n detection,evaluation,result files,model references,figures and project documentation.

## Final Project Pipeline

Underwater Images
→ Data Inspection
→ Data Preparation
→ Preprocessing
→ Image Enhancement
→ YOLOv8n Object Detection
→ Evaluation
→ Comparison
→ Error Analysis

## Datasets

Three underwater datasets were used and evaluated separately:

- **DIATAquarium.v4i.yolov8** — 11 classes
- **Aquatic Plant.v2i.yolov8** — 1 class
- **well.v8i.yolov8** — 4 classes

## Preprocessing

The finalized preprocessing configuration was:

- Image size: 640 × 640
- Color format: RGB
- Pixel normalization: 0–1
- Training augmentation:
  - Horizontal flip
  - Small rotation
  - Scale variation
  - Brightness/contrast variation
- Validation and test images were not augmented.
- Original raw datasets were preserved separately.

## Image Enhancement

The implemented classical enhancement method was:

**White Balance + CLAHE**

### White Balance

White Balance was used to reduce underwater colour distortion and colour cast.

### CLAHE

Contrast Limited Adaptive Histogram Equalization was applied to improve local contrast while limiting excessive contrast amplification.

### Enhancement Pipeline

```text
Original Image
      ↓
White Balance
      ↓
CLAHE
      ↓
Enhanced Image
