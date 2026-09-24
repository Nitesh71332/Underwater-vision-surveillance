import cv2
import numpy as np

IMAGE_SIZE=(640,640)

def resize_image(image):
    return cv2.resize(image,IMAGE_SIZE,interpolation=cv2.INTER_LINEAR)

def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

def normalize_image(image):
    return image.astype(np.float32)/255.0

def preprocess_image(image):
    image=resize_image(image)
    image=convert_bgr_to_rgb(image)
    image=normalize_image(image)
    return image

def load_and_preprocess_image(image_path):
    image=cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    return preprocess_image(image)
