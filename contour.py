import cv2
import numpy as np

def findContours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 转换为二值图
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])
    rect = np.array([[[x, y], [x + w, y], [x + w, y + h], [x, y + h]]])  # 1
    cv2.drawContours(img, [rect], -1, (255, 255, 255), 2)  # 1

    cv2.imshow("img2", img)

    cv2.waitKey()
    cv2.destroyAllWindows()


    return img

if __name__ == "__main__":
    img = cv2.imread('savergb1 .jpg')
    cv2.imshow('src', img)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[1]

    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.polylines(img, [approx], True, (0, 0, 255), 2)

    cv2.imshow('show', img)
    cv2.waitKey()

