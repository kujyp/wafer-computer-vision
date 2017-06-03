import cv2

import logging
import numpy as np

from src_0602.Logger import logger

MINIMUM_POINTS_FOR_LINE = 3

def detectContourLine(img):
    img = cv2.Canny(img, 50,150)
    lines = cv2.HoughLinesP(img, 1,np.pi/180,80,30,10)
    logger.info("lines number={}".format(len(lines)))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        img = cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


    return img