# Models
This folder contains the final YOLOv8n model checkpoints selected for the project.

## Final Models
### DIATAquarium
- Configuration: Original Image + YOLOv8n
- Model: YOLOv8n
- Epochs: 30
- Batch Size: 16
- Image Size: 640 × 640
- Model Size: approximately 5.95 MB

### Aquatic Plant
- Configuration: H03
- Pipeline: Original Image + White Balance + CLAHE + YOLOv8n
- Learning Rate: 0.0005
- Batch Size: 32
- Epochs: 30
- Optimizer: AdamW
- Image Size: 640 × 640
- Model Size: approximately 5.96 MB

### Well
- Configuration: H04
- Pipeline: Original Image + White Balance + CLAHE + YOLOv8n
- Learning Rate: 0.001
- Batch Size: 16
- Epochs: 30
- Optimizer: AdamW
- Image Size: 640 × 640
- Model Size: approximately 5.96 MB
