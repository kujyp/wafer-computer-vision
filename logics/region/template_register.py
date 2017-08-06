import cv2

import numpy as np

from config.config import Textdimens, Messages, StatusThreshold, Source
from config.consts import Status, Color
from models.calibration import Calibration
from utils.log.logging_ import logger


def regist(img, template):
    w, h = template.shape[1::-1]

    meth = 'cv2.TM_CCOEFF_NORMED'
    img = img.copy()

    method = eval(meth)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    return top_left[0]

def finddelta_withtemplate(img, template):
    normal_delta_x = (regist(img, template))
    return normal_delta_x

def finddelta(img):
    return finddelta_withtemplate(img, Calibration.getInstance().CROPPED_TEMPLATE)

def delta_status(delta):
    if delta > StatusThreshold.THRESHOLD_IN_PIXEL:
        return Status.RIGHT_ABNORMAL
    elif delta < -StatusThreshold.THRESHOLD_IN_PIXEL:
        return Status.LEFT_ABNORMAL

    return Status.NORMAL
