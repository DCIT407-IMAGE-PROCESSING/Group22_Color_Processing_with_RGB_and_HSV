# 🎨 Group 22 - Color Processing with RGB and HSV

**DCIT 407 - Image Processing | Final Project**  
**Semester 1, 2025/2026**

A comprehensive research project analyzing digital color models through systematic experiments comparing RGB and HSV color spaces, including segmentation, enhancement, and conversion validation.

---

## 👥 Team Members

| S/N | Name | Student ID |
|-----|------|------------|
| 1 | Bernard Owusu-Dankwah (Group Leader) | 11024002 |
| 2 | Albert Amoako | 11227686 |
| 3 | Desmond Owusu Ansah | 11029640 |
| 4 | Adu-Owusu Oduro | 11310750 |
| 5 | Divine Boadi (RgDivne) | 11342871 |
| 6 | Raymond Dwamena-Akenten | 11228276 |
| 7 | Angela Aboagyewaa Nyarko | 11184240 |

---

## 📋 Project Overview

This project provides rigorous experimental analysis of color image processing, systematically comparing hardware-centric RGB to perceptual-centric HSV color models. Through 30+ experiments, we demonstrate:

- ✅ **20-30% superior segmentation accuracy** with HSV under variable lighting
- ✅ **CLAHE enhancement** outperforms global histogram equalization
- ✅ **Round-trip conversion validation** with negligible error (MSE < 0.01)
- ✅ **Robust hue-based segmentation** handles wrap-around ranges effectively
- ✅ **Saturation boosting** enhances vibrancy without luminance distortion

---

## 📁 Project Structure

```
Group22_Color_Processing_with_RGB_and_HSV/
│
├── notebooks/                          # Jupyter notebooks
│   ├── main_project.ipynb             # 📘 Final comprehensive deliverable 
│   └── explorations/                   # Individual experiment notebooks
│       ├── rgb_color_model_and_histograms.ipynb
│       ├── hsv_conversion_and_segmentation.ipynb
│       ├── image_enhancement_and_applications.ipynb
│       └── color_space_conversions_analysis.ipynb
|   └── tests/           # To check the our colour processing techniques on other datasets  
│       ├── colorization.ipynb
|       └── under_water.ipynb 
|
|
├── src/                                # Python utility modules
│   ├── color_utils.py                 # Color space conversions (RGB↔HSV, RGB↔CMY)
│   ├── visualization.py               # Image display and comparison functions
│   └── image_processing.py            # Segmentation, CLAHE, pseudo-coloring
│
├── images/
│   └── input/                          # Test images
│       ├── peppers.jpg                # RGB color analysis benchmark
│       ├── beans.tiff                 # HSV segmentation testing
│       ├── foggy.jpg                  # Enhancement demonstrations
│       └── fruits.jpg                 # Additional test image
|    └── under_water/                     # This was used in the under_water.ipynb [dataset link](https://drive.google.com/drive/folders/19ScbxkyXWpW4Hkf_Kv_z8MpTif_pepBo?usp=sharing)
│       └── *.png
|    └── colorization/                     # This was used in the under_water.ipynb [dataset link](https://drive.google.com/drive/folders/1QI-hzXQrl0YVfq0eSXRXkZRh9KasSyvo?usp=sharing)
│       └── *.jpg
|
│
├── .venv/                              # Virtual environment (not tracked)
├── .gitignore                          # Git ignore rules
├── requirements.txt                    # Python dependencies
└── README.md                          # This file
```


---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (tested with Python 3.13.2)
- **pip** package manager
- **Jupyter Notebook** or **VS Code** with Jupyter extension

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DCIT407-IMAGE-PROCESSING/Group22_Color_Processing_with_RGB_and_HSV.git
   cd Group22_Color_Processing_with_RGB_and_HSV
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Core dependencies:**
   - `opencv-python==4.13.0.92` - Image processing operations
   - `numpy==2.4.2` - Array computations
   - `pandas==3.0.0` - Data analysis and tables
   - `matplotlib==3.10.8` - Visualization
   - `scipy==1.15.1` - Entropy calculations
   - `jupyter==1.1.1` - Notebook environment

4. **Verify installation**
   ```bash
   python -c "import cv2, numpy, pandas; print('✓ All dependencies installed')"
   ```

---

## 💻 How to Run

### Option 1: Run the Main Project Notebook (Recommended)

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Navigate to** `notebooks/main_project.ipynb`

3. **Run all cells** (`Kernel > Restart & Run All`) or execute cells sequentially

4. **Expected output:**
   - Environment configuration confirmation
   - Loaded images (peppers, beans, foggy, fruits)
   - 16 experiments with visualizations
   - Performance metrics and comparison tables
   - Round-trip validation results

### Option 2: Run Individual Exploration Notebooks

```bash
cd notebooks/explorations
jupyter notebook rgb_color_model_and_histograms.ipynb
```

### Option 3: Use Python Scripts

```python
from src.color_utils import bgr_to_hsv, hsv_to_bgr
from src.visualization import compare_results
from src.image_processing import segment_color
import cv2 as cv

# Load image
img = cv.imread('images/input/peppers.jpg')

# Convert to HSV
hsv = bgr_to_hsv(img)

# Segment yellow regions
yellow_mask = segment_color(hsv, [20, 100, 100], [35, 255, 255])
```

---

## 📊 Key Experiments

The `main_project.ipynb` contains 10 major sections:

1. **Setup & Environment** - Library imports, path configuration
2. **Dataset Ingestion** - Image loading and metadata analysis
3. **RGB Analysis** - Pure colors, additive mixing, channel decomposition, histograms
4. **HSV Processing** - Hue manipulation, color segmentation, illumination robustness
5. **Alternative Color Spaces** - CMY, L\*a\*b\*, YCbCr conversions
6. **Image Enhancement** - CLAHE, saturation boosting, pseudo-coloring
7. **Performance Benchmarking** - Timing, entropy metrics, contrast analysis
8. **Comparative Analysis** - RGB vs HSV comparison tables
9. **Conclusions** - Key findings, recommendations, limitations
10. **References & Appendix** - Documentation and experimental parameters

---

## 🔬 Research Findings

### Color Segmentation Performance
- **HSV superiority confirmed**: 20-30% improvement over RGB
- **Illumination robustness**: 40-50% better stability under varying lighting
- **Red segmentation**: Multi-range masking handles wraparound (0-10° + 170-180°)

### Enhancement Techniques
- **CLAHE optimization**: 15-20% contrast gain over global methods
- **Saturation boosting**: 1.3× factor produces vibrant results without clipping

### Conversion Validation
- **Round-trip fidelity**: BGR→HSV→BGR maintains MSE < 0.01 (PSNR > 50 dB)
- **Performance overhead**: <1 ms per conversion (negligible)

---

## 🛠️ Troubleshooting

### Import Errors
If you see `ModuleNotFoundError: No module named 'src'`:
```python
import sys
from pathlib import Path
project_root = Path.cwd().resolve().parent
sys.path.insert(0, str(project_root))
```

### Image Not Found
Ensure images are in `images/input/`:
```
images/input/peppers.jpg
images/input/beans.tiff
images/input/foggy.jpg
images/input/fruits.jpg
```

### Kernel Issues in Jupyter
```bash
python -m ipykernel install --user --name=venv
```

---

## 📖 Additional Resources

For more information about color space theory and image processing concepts, refer to academic literature on computer vision and digital image processing.

---

## 📝 License

This project is submitted as academic coursework for DCIT 407 - Image Processing.

---

##  Acknowledgments

- **Course Instructor** for guidance on color space theory
- **OpenCV Community** for comprehensive documentation
- **Team Members** for collaborative effort in experimental design

---
