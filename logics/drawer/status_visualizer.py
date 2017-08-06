import cv2

import numpy as np

from config.config import Source, Textdimens
from config.consts import Color
from utils.calibration.calibration import Calibration


def show_calibrated_rectangle(image, seg, color=Color.BLUE):
    copy = np.copy(image)
    TEMPLATE_POSITION = Calibration.getInstance().CROPPED_TEMPLATEPOSITION_INPIXEL
    XSIZEOFTEMPLATE = TEMPLATE_POSITION[Source.XEND] - TEMPLATE_POSITION[Source.XSTART]
    xst, xed = TEMPLATE_POSITION[Source.XSTART], TEMPLATE_POSITION[Source.XSTART] + (XSIZEOFTEMPLATE)
    yst, yed = 0, image.shape[0]

    delta = seg - TEMPLATE_POSITION[Source.XSTART]

    cv2.rectangle(copy, (xst, yst), (xed, yed), color, 3)
    cv2.putText(copy,
                "Normal",
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                color,
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)
    cv2.putText(copy,
                "x=[{}-{}]".format(xst, xed),
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 2 + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                color,
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    cv2.putText(copy, "delta={}".format(delta),
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 3 + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                color,
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    return copy

def show_statusmessage(image, result_msg, position, color):
    (xst, yst, xed, yed) = position
    clone = np.copy(image)

    cv2.putText(clone,
                result_msg,
                (xed + Textdimens.TEXT_X_MARGIN, yst + Textdimens.TEXT_LINESPACING * 4 + Textdimens.TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX,
                Textdimens.TEXT_FONTSIZE,
                color,
                Textdimens.TEXT_LINEWIDTH,
                cv2.LINE_AA)

    return clone