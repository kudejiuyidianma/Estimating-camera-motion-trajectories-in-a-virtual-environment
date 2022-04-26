import numpy as np
import cv2
import datetime

starttime = datetime.datetime.now()
line = cv2.VideoWriter('route.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 5.0, (512, 512))
num_list = []
with open('data1.txt') as file_obj:
    content = file_obj.readlines()
    for j in range(0, len(content)):
        num = content[j].split('\n')
        num_list.append(int(num[0]))

img = np.zeros((512, 512, 3), np.uint8)
for i in range(0, len(num_list)):
    cv2.circle(img, (256, num_list[i]), 2, (0, 255, 0), 4)
    line.write(img)
    i += 1

endtime = datetime.datetime.now()
print((endtime - starttime)*100)