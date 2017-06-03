#-*- coding: utf-8 -*-

import cv2
import sys
import numpy as np
import os
from src import process


def load_allpath(path):
    res = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file[0] is '.':
                continue
            filepath = os.path.join(root, file)
            res.append(filepath)
    return res


res = load_allpath("data/내려놓은후_모든사진")
res = [res[0]]

for filepath in res:
    img = cv2.imread(filepath)

    img = process.drawcontour(img)
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow('video',img)
    cv2.waitKey(0)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
#video_capture.release()
cv2.destroyAllWindows()