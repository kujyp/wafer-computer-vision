#-*- coding: utf-8 -*-

import cv2
import os


res = ["data/mpg인코딩/ch01 Lup ch1.mpg"]

for path in res:
    video_capture = cv2.VideoCapture(path)


    while True:
        ret, frame = video_capture.read()

        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        cv2.imshow('video',frame)
        #cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()