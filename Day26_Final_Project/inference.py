from ultralytics import YOLO


def load_model(model_path):
    return YOLO(model_path)


def run_inference(model,image_path,conf=0.25,imgsz=640):
    results=model.predict(
        source=image_path,
        conf=conf,
        imgsz=imgsz,
        verbose=False
    )

    return results


def extract_detections(results):
    detections=[]

    for result in results:
        boxes=result.boxes

        if boxes is None:
            continue

        for i in range(len(boxes)):
            xyxy=boxes.xyxy[i].cpu().numpy().tolist()
            confidence=float(boxes.conf[i].cpu().item())
            class_id=int(boxes.cls[i].cpu().item())

            class_name=result.names[class_id]

            detections.append({
                "class_id":class_id,
                "class_name":class_name,
                "confidence":confidence,
                "bbox":xyxy
            })

    return detections


def detect_image(model_path,image_path,conf=0.25,imgsz=640):
    model=load_model(model_path)

    results=run_inference(
        model,
        image_path,
        conf=conf,
        imgsz=imgsz
    )

    detections=extract_detections(results)

    return detections
