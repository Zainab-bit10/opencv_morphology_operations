# OpenCV Morphological Operations

A Python demonstration of basic and advanced morphological image processing techniques using OpenCV and NumPy.

## Features
- **Erosion & Dilation:** Basic operations to erode or dilate boundaries of foreground objects.
- **Opening & Closing:** Noise removal (opening) and filling small holes/gaps (closing).
- **Morphological Gradient:** Edge extraction via the difference between dilation and erosion.
- **Top Hat & Black Hat:** Isolation of elements brighter or darker than their surroundings based on the kernel size.

## Prerequisites
Ensure Python is installed along with the following packages:
```bash
pip install opencv-python numpy
