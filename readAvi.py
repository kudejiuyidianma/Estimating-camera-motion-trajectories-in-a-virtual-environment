import cv2
import numpy as np

def findContours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 转换为二值图
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    rect = cv2.minAreaRect(contours[0])
    points = cv2.boxPoints(rect)
    points = np.int0(points)
    cv2.drawContours(img, [points], 0, (255, 255, 255), 2)

    cv2.imshow("img2", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
if __name__ == "__main__":

    cap = cv2.VideoCapture("savesn.avi")

    if cap.isOpened():  #VideoCaputre对象是否成功打开
        print('已经打开了视频文件')
        fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 返回视频的宽
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 返回视频的高
        print('fps:', fps, 'width:', width, 'height:', height)
        i = 0
        list = []
        while 1:
            success, frame = cap.read()
            if success:
                i = i+1
                file_name = 'savergb' + str(i) + ' .jpg'
                cv2.imwrite(file_name, frame)
            else:
                break

    else:
        print('视频文件打开失败')




