import cv2
import numpy as np

def generate_pure_color(color_name, size=(256, 256)):
    """
    Generate pure BGR patches for fundamental additive and subtractive colors.
    """
    colors = {
        'red': [0, 0, 255], 'green': [0, 255, 0], 'blue': [255, 0, 0],
        'yellow': [0, 255, 255], 'magenta': [255, 0, 255], 'cyan': [255, 255, 0],
        'white': [255, 255, 255], 'black': [0, 0, 0]
    }
    img = np.zeros((*size, 3), dtype=np.uint8)
    img[:, :] = colors.get(color_name.lower(), [0, 0, 0])
    return img

def bgr_to_hsv(image):
    """Convert BGR image to HSV space."""
    if image is None: raise ValueError("Image not found.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def hsv_to_bgr(image):
    """Convert HSV image back to BGR space."""
    return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

def bgr_to_rgb(image):
    """Convert BGR to RGB for matplotlib display."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def rgb_to_cmy(image):
    """
    Convert RGB to CMY (subtractive model). 
    Formula: C = 1-R, M = 1-G, Y = 1-B.
    """
    norm_img = image.astype(np.float32) / 255.0
    return 1.0 - norm_img