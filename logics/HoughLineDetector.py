import cv2

import numpy as np

from utils.Logger import logger


def detectHoughLines(image):
    img = image[:]
    img = cv2.Canny(img, 50,150)
    lines = cv2.HoughLinesP(img, 1,np.pi/180,80,30,10)
    logger.debug("lines number={}".format(len(lines)))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    from logics.ContourLineDetector import findMainDirectionByLines
    mainDirection = findMainDirectionByLines(lines)
    mask = np.zeros(img.shape)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(mask, (x1, y1), (x2, y2), (255, 255, 255), 2)

    return mask, mainDirection