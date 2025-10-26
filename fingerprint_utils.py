import cv2
import hashlib
import numpy as np

def preprocess_fingerprint(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

def hash_fingerprint(image_path):
    img = preprocess_fingerprint(image_path)
    resized = cv2.resize(img, (128, 128))
    flat = resized.flatten()
    fingerprint_bytes = flat.tobytes()
    hash_value = hashlib.sha256(fingerprint_bytes).hexdigest()
    return hash_value
