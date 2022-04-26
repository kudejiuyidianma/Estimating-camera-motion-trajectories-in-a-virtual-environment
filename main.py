import datetime

import cv2
import numpy as np

def filter_out(src_frame):
    if src_frame is not None:
        hsv = cv2.cvtColor(src_frame, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 0])
        upper = np.array([180, 255, 100])

        mask = cv2.inRange(hsv, lower, upper)
        return cv2.bitwise_and(src_frame, src_frame, mask=mask)

def pic(image):
    roi = image[320:512, 180:300]

    #cv2.imshow('roi', roi)
    #cv2.waitKey(0)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # blur and threshold the image
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    cnt = c[0]
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
    center = (int(w/2+x+250), int(h/2 + y+180))

    return image, center

if __name__ == "__main__":
    starttime = datetime.datetime.now()
    cap = cv2.VideoCapture("savergb.avi")
    if cap.isOpened():  # VideoCaputre对象是否成功打开
        print('已经打开了视频文件')
        fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 返回视频的宽
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 返回视频的高
        print('fps:', fps, 'width:', width, 'height:', height)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video = cv2.VideoWriter('rgb1.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 5.0, (512, 512))
        i = 0
        while 1:
            success, frame = cap.read()
            if success:
                i = i + 1
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = filter_out(frame)
                frame, center = pic(frame)
                data = np.load('3d.npy')
                data_i = data[i-1]
                x_i = center[0]
                y_i = center[1]
                data_i_c = data_i[x_i][y_i][2]
                font = cv2.FONT_HERSHEY_SIMPLEX  # 使用默认字体
                im = np.zeros((50, 50, 3), np.uint8)
                frame = cv2.putText(im, str(data_i_c), (0, 40), font, 1.2, (255, 255, 255),
                                  2)  # 添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细

                #num = -int(data_i_c*100)
                #f = open('data1.txt', 'a')
                #f.write(str(num))
                #f.write('\n')
                #f = open('data2.txt', 'a')
                #f.write(str(data_i_c))
                #f.write('\n')
                video.write(frame)
            else:
                break

    else:
        print('视频文件打开失败')
    endtime = datetime.datetime.now()
    print((endtime - starttime)*100)
