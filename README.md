# cv2 Image Scan
Tuning HSV values to find objects of particular colour ranges using cv2/python3.

# Before you get started
- Understanding of basic python
- HSV colour space

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/cv2-hsv-tuning.git
```
**Modules/dependencies:**
- `cv2`

Install the following dependences:
```sh
pip install cv2
```

Running:
- Set the path in `main.py` to your image
- Enter `python3 main.py` in terminal
- Move sliders in trackbar to view resulting contours/mask

# Tests
- Showing original image, mask and result on screen dynamically
- Moving trackbar sliders to locate object of interest

# Contributors
- Daniel Corcoran

# Screenshots

### Trackbar GUI
GUI for variable input. Includes HSV upper and lower values as well as a range for size of contours to include in Frame.
![](https://github.com/danielc92/cv2-hsv-tuning/blob/master/screenshots/trackbar_screenshot_01.04.2019.png)
### Frame
Shows original image with contour layer overlay.
![](https://github.com/danielc92/cv2-hsv-tuning/blob/master/screenshots/frame_screenshot__01.04.2019.png)
### Mask
A filter layer representing the HSV filter calculated from trackbar GUI.
![](https://github.com/danielc92/cv2-hsv-tuning/blob/master/screenshots/mask_screenshot_01.04.2019.png)
### Result
Results with colour.
![](https://github.com/danielc92/cv2-hsv-tuning/blob/master/screenshots/result_screenshot_01.04.2019.png)

# Sources
- [Code snippet from pysource](https://pysource.com/2018/01/31/object-detection-using-hsv-color-space-opencv-3-4-with-python-3-tutorial-9/)
- [Object detection using HSV Color space – OpenCV 3.4 with python 3 Tutorial 9](https://www.youtube.com/watch?v=SJCu1d4xakQ)
