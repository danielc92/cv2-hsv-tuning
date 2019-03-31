import cv2
import numpy as np
 
def nothing(x):
    pass

# ignore video capture for now, this script will focus on static images
# cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("Lower Hue", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower Saturation", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper Saturation", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Trackbars", 255, 255, nothing)
 
 
while True:
    # ignore video capture for now, this script will focus on static images
    # _, frame = cap.read()
    frame = cv2.imread('./gh-repos/pool-detection/data/20190108_WGS84_S_Mercator_144_98370_-37_90363_144_98628_-37_90264_20.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # Store trackbar variables
    lower_hue = cv2.getTrackbarPos("Lower Hue", "Trackbars")
    lower_saturation = cv2.getTrackbarPos("Lower Saturation", "Trackbars")
    lower_value = cv2.getTrackbarPos("Lower Value", "Trackbars")
    upper_hue = cv2.getTrackbarPos("Upper Hue", "Trackbars")
    upper_saturation = cv2.getTrackbarPos("Upper Saturation", "Trackbars")
    upper_value = cv2.getTrackbarPos("Upper Value", "Trackbars")
 
    # lower_hsv_range = np.array([lower_hue, lower_saturation, lower_value])
    # upper_hsv_range = np.array([upper_hue, upper_saturation, upper_value])
    mask = cv2.inRange(hsv, [lower_hue, lower_saturation, lower_value], [upper_hue, upper_saturation, upper_value])
 
    result = cv2.bitwise_and(frame, frame, mask=mask)
 
    # Show the frame, mask and result 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
 
    # Break out of this while loop on 'escape' press
    key = cv2.waitKey(1)
    if key == 27:
        break

# ignore video capture for now, this script will focus on static images
# cap.release()
cv2.destroyAllWindows()