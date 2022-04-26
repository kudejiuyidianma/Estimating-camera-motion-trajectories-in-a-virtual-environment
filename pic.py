import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
cv2.circle(img, (256, 256), 2, (0, 255, 0), 4)
cv2.imshow('img', img)
cv2.waitKey(0)