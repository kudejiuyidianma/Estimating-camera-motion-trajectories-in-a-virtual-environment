#!-*-coding:utf-8 -*-
# !@Time: 2021/5/24 15:16
# !@Author :skl

import cv2
# import schedule
import time,datetime
import socket
import os
import sys
import struct
from socket import *




def save_video(save_path):
    number_frame = 0
    cap = cv2.VideoCapture("tcp://192.168.1.105:40921")
    # cap = cv2.VideoCapture(1)
    cap.set(3, 1920)
    cap.set(4, 1080)
    frame_rates = 25.0
    cv2.namedWindow('video', 0)
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')  #norm
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')  # smaller
    # fourcc = cv2.VideoWriter_fourcc('T', 'H', 'E', 'O')  #Encoder not found  ('P', 'I', 'M', 'I')
    # fourcc = cv2.VideoWriter_fourcc('F', 'L', 'V', '1')  # norm+
    out = cv2.VideoWriter(save_path, fourcc, frame_rates, (1920, 1080))
    success, frame = cap.read()

    BUFFSIZE = 2048
    ADDR = (('192.168.1.102',7789))
    # tctimeClient = socket(AF_INET, SOCK_STREAM)
    # tctimeClient.connect(ADDR)

    while (success):
        # print(1)
        number_frame = number_frame + 1
        cv2.imshow('video', frame)
        a = out.write(frame)
        result = False
        ##3
        if result:
            data = '111'
            tctimeClient.send(data.encode())
            data = tctimeClient.recv(BUFFSIZE).decode()
            if not data: break # data为空
            print(data)

        key = cv2.waitKey(10)
        if key == 27:
            break
        success, frame = cap.read()
    # tctimeClient.close()
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    save_video('test1.avi')

