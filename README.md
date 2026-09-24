# Underwater Vision-Based Surveillance

Internship project focused on underwater image enhancement and object detection using Machine Learning and Artificial Intelligence.

## Datasets

- well.v8i.yolov8 — 4 classes
- DIATAquarium.v4i.yolov8 — 11 classes
- Aquatic Plant.v2i.yolov8 — 1 class

All three datasets are evaluated separately.

## Project Pipeline

Underwater Images → Data Inspection → Data Preparation → Preprocessing → Image Enhancement → YOLO Object Detection → Evaluation → Comparison → Error Analysis

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
- Model size
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
- Day 23 — Final Validation & Performance Comparison
- Day 24 — Project Progress / Documentation
- Day 25 — Error & Failure Analysis
- Day 26 — Final Software Package & Documentation
- Day 27 — Mentor Review & Technical Sign-Off
- Day 28 — Peer Mock Presentation & Final Submission

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
- Final validation and available test-set evaluation completed
- Runtime and model-size measurements completed
- Error and failure analysis completed
- Final preprocessing, enhancement, detection and evaluation code packaged
- Final project documentation and README completed
- Final project figures and selected prediction outputs prepared
- Mentor review completed and technical results approved
- Peer mock presentation completed
- Repository and final project artefacts verified for submission
- Final individual project package completed
- No video data is currently available, so tracking is not included in the implementation

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
- Optimizer: AdamW
- Precision: 95.4%
- Recall: 96.1%
- mAP@0.5: 98.5%
- mAP@0.5:0.95: 71.5%

### Well

- Pipeline: Original Image + White Balance + CLAHE + YOLOv8n
- Learning Rate: 0.001
- Batch Size: 16
- Epochs: 30
- Optimizer: AdamW
- Precision: 35.7%
- Recall: 40.1%
- mAP@0.5: 36.8%
- mAP@0.5:0.95: 16.8%

## Final Test Results

### Aquatic Plant

- Precision: 97.99%
- Recall: 90.26%
- mAP@0.5: 96.75%
- mAP@0.5:0.95: 71.12%

### Well

- Precision: 43.00%
- Recall: 37.46%
- mAP@0.5: 39.34%
- mAP@0.5:0.95: 16.15%

### DIATAquarium

The supplied local DIATAquarium copy did not contain a separate test set. Therefore, the available validation set was used for the final reported evaluation.

## Runtime & Model Size

| Dataset | Inference Time/Image | FPS | Model Size |
|---|---:|---:|---:|
| DIATAquarium | 22.14 ms | 45.16 | 5.95 MB |
| Aquatic Plant | 9.80 ms | 102.02 | 5.96 MB |
| Well | 9.98 ms | 100.21 | 5.96 MB |

Runtime represents YOLO inference time and does not include separate White Balance + CLAHE preprocessing time.

## Key Findings

White Balance + CLAHE did not consistently improve YOLOv8n detection across all three datasets. Its effect was dataset- and class-dependent.

- Aquatic Plant showed mixed test-set changes, with Precision and mAP@0.5:0.95 increasing while Recall and mAP@0.5 decreased compared with the original baseline.
- DIATAquarium showed decreased detection performance with WB+CLAHE during the comparative analysis.
- Well showed lower performance than the original baseline on all four final test metrics.
- Dataset imbalance and source-level overlap remain important limitations.
- The local DIATAquarium copy does not contain a separate test set, so its final evaluation is based on the available validation set.
- Hyperparameter selection was performed using validation performance, with mAP@0.5:0.95 as the primary selection metric.
- Validation-based model selection did not always result in improved test-set performance.
- Error analysis identified haze, low visibility, small objects, edge-located objects, class confusion and class imbalance as recurring difficult conditions.

## Error Analysis

### DIATAquarium

- Fish/Fishes class confusion
- Possible missed Camera detection
- Low-confidence predictions
- Haze and low-visibility scenes

### Aquatic Plant

- Missed plant detections
- Low-confidence predictions
- Haze and unclear plant boundaries

### Well

- Small and edge-located objects
- Difficult stone detections
- Class imbalance
- Possible false positives

## Limitations

- The local DIATAquarium copy does not contain a separate test set.
- Source-level overlap was identified across dataset splits.
- The Well dataset contains strong class imbalance.
- Error analysis covered representative difficult cases rather than every prediction.
- The exact cause of individual detection failures cannot always be confirmed from visual inspection alone.
- WB+CLAHE was evaluated as a combined enhancement method, so the individual contribution of White Balance and CLAHE was not isolated.
- Water-Net and FUnIE-GAN were reviewed during the literature study but were not implemented.
- Tracking was excluded because video data was not available.

## Final Project Scope

The final implementation focuses on:

**Underwater Image Enhancement → YOLOv8n Object Detection → Performance Evaluation → Error Analysis**

All three supplied datasets are evaluated separately.

Tracking is outside the current implementation scope because video data is not available.

## Final Software Package

The final project package contains:

- `preprocessing/` — preprocessing implementation
- `enhancement/` — White Balance + CLAHE implementation
- `detection/` — YOLOv8n inference implementation
- `evaluation/` — evaluation utilities
- `models/` — final model references and model documentation
- `results/` — final results and comparison tables
- `figures/` — selected training, prediction and error-analysis figures
- `docs/` — project documentation
- `README.md` — project overview and usage information
- `requirements.txt` — required Python packages

## Final Artifacts

The final project includes:

- Final model checkpoints
- Frozen configuration file
- Final model summary
- Dataset preparation and preprocessing documentation
- Enhancement implementation
- YOLOv8n training and evaluation results
- Runtime and model-size results
- Comparison and analysis
- Prediction outputs
- Error-analysis outputs
- Final project documentation
- Day-wise internship documentation
- Final presentation
- Final report

## Reproducibility

The project package documents:

- Dataset structure
- Preprocessing configuration
- Enhancement method
- YOLOv8n model configuration
- Training parameters
- Evaluation metrics
- Final model configurations
- Runtime measurements
- Error-analysis observations
- Required software packages

The final project package was verified before submission.

## Mentor Review & Approval

- Final methodology reviewed: Approved
- Final results reviewed: Approved
- Final model configurations reviewed: Approved
- Error analysis reviewed: Approved
- Documentation reviewed: Approved
- Final presentation reviewed: Approved
- Technical results: Frozen
- Major corrections required: None

## Day 28 — Final Submission

- Individual peer mock presentation completed
- Presentation timing and clarity reviewed
- Technical choices prepared for discussion and defense
- GitHub repository verified
- Dataset and model references verified
- Reproducibility information verified
- Final report completed
- Final PPT completed
- Final software package completed
- Final models and outputs verified
- Final project package prepared for submission

## Future Scope

- Implement and compare learning-based enhancement methods such as Water-Net and FUnIE-GAN.
- Investigate improved handling of severe class imbalance.
- Improve small-object detection.
- Investigate source-independent dataset splitting.
- Evaluate additional underwater datasets.
- Explore advanced underwater object detection architectures.
- Add video-based object tracking when sequential/video data becomes available.
- Investigate more robust enhancement-detection combinations.

## Final Conclusion

The project developed an end-to-end underwater vision pipeline combining image preprocessing, underwater image enhancement and YOLOv8n object detection.

Experiments across the three supplied datasets showed that White Balance + CLAHE does not consistently improve detection performance. The effect varies according to dataset characteristics, object classes, visibility conditions and class distribution.

The final project package contains the implemented pipeline, final model checkpoints, evaluation results, documentation, selected outputs and reproducibility information.

## Final Status

**Project:** Completed  
**Mentor Review:** Approved  
**Technical Results:** Frozen  
**Final Presentation:** Completed  
**Repository Verification:** Completed  
**Final Submission Package:** Completed

**Author:** C. Nitesh Kumar
