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

def apply_hsv_transfer(grayscale_target, reference_img):
    ref_hsv = cv2.cvtColor(reference_img, cv2.COLOR_BGR2HSV)
    mean_h = np.mean(ref_hsv[:,:,0])
    mean_s = np.mean(ref_hsv[:,:,1])
    
    if len(grayscale_target.shape) == 3:
        target_v = cv2.cvtColor(grayscale_target, cv2.COLOR_BGR2GRAY)
    else:
        target_v = grayscale_target
        
    h = np.full_like(target_v, mean_h, dtype=np.uint8)
    s = np.full_like(target_v, mean_s, dtype=np.uint8)
    
    return cv2.cvtColor(cv2.merge([h, s, target_v]), cv2.COLOR_HSV2BGR)

def apply_sepia_filter(image):
    img_float = np.array(image, dtype=np.float64)
    matrix = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    img_sepia = cv2.transform(img_float, matrix)
    img_sepia = np.clip(img_sepia, 0, 255)
    return img_sepia.astype(np.uint8)