import cv2
import numpy as np


def nothing(x):
    pass


# create black img, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Image")

# create trackbar for color change
cv2.createTrackbar("R", "Image", 0, 255, nothing)
cv2.createTrackbar("G", "Image", 0, 255, nothing)
cv2.createTrackbar("B", "Image", 0, 255, nothing)

# create switch for on/off functionality
switch = '0 : off\n1 : on'
cv2.createTrackbar(switch, "Image", 0, 1, nothing)

while(1):
    cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    s = cv2.getTrackbarPos(switch, "Image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()