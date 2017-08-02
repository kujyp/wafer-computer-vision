import cv2

import numpy as np

from config.config import Textdimens, Messages
from config.consts import Status
from models.calibration import Calibration
from utils.log.logging_ import logger


def regist(img, template):
    w, h = template.shape[1::-1]

    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #       'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    meth = 'cv2.TM_CCOEFF_NORMED'
    #img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    #template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    #for meth in methods:
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
    return finddelta_withtemplate(img, Calibration.getInstance().cropped_template)

def drawNormalRectangle(image, seg):
    copy = np.copy(image)
    templatex = 845
    xst, xed = templatex, templatex+(1130-845) # Video4 Normal
    yst, yed = 0, image.shape[0]

    delta = seg - templatex

    cv2.rectangle(copy, (xst, yst), (xed, yed), (255, 0, 0), 3)
    cv2.putText(copy,
                "Normal",
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                (255, 0, 0),
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)
    cv2.putText(copy,
                "x=[{}-{}]".format(xst, xed),
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 2 + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                (255, 0, 0),
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    cv2.putText(copy, "delta={}".format(delta),
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 3 + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                (0, 0, 255),
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    result_msg = ""
    if deltaStatus(delta) == Status.NORMAL:
        result_msg = Messages.ON_NORMAL
    elif deltaStatus(delta) == Status.RIGHT_ABNORMAL:
        result_msg = Messages.ON_RIGHT_ABNORMAL
    elif deltaStatus(delta) == Status.LEFT_ABNORMAL:
        result_msg = Messages.ON_LEFT_ABNORMAL

    cv2.putText(copy,
                result_msg,
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 4+ Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                (0, 0, 255),
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    logger.info("delta={}, result={}".format(delta,result_msg))

    return copy

def deltaStatus(delta):
    if delta > 20:
        return Status.RIGHT_ABNORMAL
    elif delta < -20:
        return Status.LEFT_ABNORMAL

    return Status.NORMAL
