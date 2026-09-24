from ultralytics import YOLO


def validate_model(model_path,data_yaml,split="val",imgsz=640,batch=16,device=0):
    model=YOLO(model_path)

    results=model.val(
        data=data_yaml,
        split=split,
        imgsz=imgsz,
        batch=batch,
        device=device,
        verbose=False
    )

    return results


def get_metrics(results):
    return {
        "precision":float(results.box.mp),
        "recall":float(results.box.mr),
        "mAP50":float(results.box.map50),
        "mAP50_95":float(results.box.map)
    }


def evaluate_model(model_path,data_yaml,split="val",imgsz=640,batch=16,device=0):
    results=validate_model(
        model_path,
        data_yaml,
        split,
        imgsz,
        batch,
        device
    )

    metrics=get_metrics(results)

    return metrics
