import numpy as np
import cv2

if __name__ == "__main__":

    cap = cv2.VideoCapture("savesn.avi")

    if cap.isOpened():  #VideoCaputre对象是否成功打开
        print('已经打开了视频文件')
        #fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率
        fps = 500
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 返回视频的宽
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 返回视频的高
        print('fps:', fps, 'width:', width, 'height:', height)
        i = 0
        while i < 1:
            success, frame = cap.read()
            if success:
                i = i+1
                file_name = 'savergb' + str(i) + '.jpg'
            else:
                break

    else:
        print('视频文件打开失败')




