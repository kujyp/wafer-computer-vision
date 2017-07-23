import cv2

import numpy as np

from models.line import Line


def detectHoughLines(image):
    img = np.copy(image)
    # img = cv2.Canny(img, 50,150)
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lines = cv2.HoughLinesP(img, 1, np.pi / 180, 80, 30, 10)
    # logger.debug("lines number={}".format(len(lines)))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # from logics.contour.contour_line_detector import findMainDirectionByLines
    # maindirectionline = findMainDirectionByLines(lines)
    # from logics.contour.contour_line_detector import findMainLines
    # mainline = findMainLines(lines, maindirectionline)
    mask = np.zeros(img.shape)
    maskwithlines = Line.drawLines(mask, lines)
    imagewithlines = Line.drawLines(image, lines)
    mainline = None
    # mainline = Line.drawLines(image, mainline.baseline)

    return maskwithlines, imagewithlines, mainline