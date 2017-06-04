import cv2

import numpy as np

from models.line import Line
from utils.logging_ import logger
from utils.visualize.windowmanager import WindowManager


def detectHoughLines(image):
    img = image[:]
    img = cv2.Canny(img, 50,150)
    lines = cv2.HoughLinesP(img, 1,np.pi/180,80,30,10)
    # logger.debug("lines number={}".format(len(lines)))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    from logics.contour_line_detector import findMainDirectionByLines
    maindirectionline = findMainDirectionByLines(lines)
    from logics.contour_line_detector import findMainLines
    mainline = findMainLines(lines, maindirectionline)
    mask = np.zeros(img.shape)
    mask = Line.drawLines(mask, mainline.baseline)
    WindowManager.getInstance().imgshow(mask, '2')
    third = Line.drawLines(mask, lines)
    WindowManager.getInstance().imgshow(third, '3')
    fourth = Line.drawLines(image, mainline.baseline)
    WindowManager.getInstance().imgshow(fourth , '4')

    return mask, mainline