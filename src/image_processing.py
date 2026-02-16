import cv2
import numpy as np

def segment_color(hsv_image, lower_range, upper_range):
    """Isolate specific colors using HSV thresholding."""
    mask = cv2.inRange(hsv_image, np.array(lower_range), np.array(upper_range))
    return mask

def apply_clahe(image, clip_limit=2.0, tile_grid=(8, 8)):
    """Apply Contrast Limited Adaptive Histogram Equalization to the V channel."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid)
    v_enhanced = clahe.apply(v)
    return cv2.cvtColor(cv2.merge([h, s, v_enhanced]), cv2.COLOR_HSV2BGR)

def equalize_v_channel(image):
    """Global histogram equalization on the Value channel to preserve Hue."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_eq = cv2.equalizeHist(v)
    return cv2.cvtColor(cv2.merge([h, s, v_eq]), cv2.COLOR_HSV2BGR)

def pseudo_color(gray_image, colormap='jet'):
    """Map grayscale intensities to color for better human visualization."""
    cmaps = {'jet': cv2.COLORMAP_JET, 'hot': cv2.COLORMAP_HOT, 'cool': cv2.COLORMAP_COOL}
    return cv2.applyColorMap(gray_image, cmaps.get(colormap, cv2.COLORMAP_JET))