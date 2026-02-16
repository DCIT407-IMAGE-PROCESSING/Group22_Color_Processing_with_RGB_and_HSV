import matplotlib.pyplot as plt
import cv2

def show_image(image, title="Image", cmap=None, figsize=(6, 6)):
    """Display a single image (handles BGR/RGB swap automatically)."""
    plt.figure(figsize=figsize)
    if len(image.shape) == 3:
        # OpenCV uses BGR, Matplotlib uses RGB
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(image, cmap=cmap or 'gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def compare_results(images, titles, figsize=(15, 5), cmap=None):
    """Display multiple images side-by-side for comparative analysis."""
    n = len(images)
    fig, axes = plt.subplots(1, n, figsize=figsize)
    if n == 1: axes = [axes]
    
    for ax, img, title in zip(axes, images, titles):
        if len(img.shape) == 3:
            ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            ax.imshow(img, cmap=cmap or 'gray')
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def plot_histogram(image, title="RGB Histogram"):
    """Plot frequency distribution of pixel intensities for each channel."""
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 4))
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=f'{col.upper()} channel')
    plt.xlim([0, 256])
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()