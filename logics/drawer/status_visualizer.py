import cv2

import numpy as np

from config.config import Source, Textdimens
from config.consts import Color, InNumpyarray


def show_calibrated_rectangle(image, positionx, color=Color.BLUE):
    """
    Calibarted_Template위치에 사각형을 그러줍니다.
     
    :param image: 원본 이미지
    :param positionx: 추출된 기둥의 위치 X좌표
    :param color: 그려질 사각형의 선 색깔
    :return: 출력된 이미지
    """
    copy = np.copy(image)
    from utils.calibration.calibration import Calibration
    TEMPLATE_POSITION = Calibration.getInstance().CROPPED_TEMPLATEPOSITION_INPIXEL
    XSIZEOFTEMPLATE = TEMPLATE_POSITION[Source.XEND] - TEMPLATE_POSITION[Source.XSTART]
    xst, xed = TEMPLATE_POSITION[Source.XSTART], TEMPLATE_POSITION[Source.XSTART] + (XSIZEOFTEMPLATE)
    yst, yed = 0, image.shape[InNumpyarray.Y]

    delta = positionx - TEMPLATE_POSITION[Source.XSTART]

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
    """
    화면에 StatusMessage를 출력합니다
    
    :param image: 원본 이미지
    :param result_msg: 출력 메세지
    :param position: 출력 위치
    :param color: 출력 색깔
    :return: 출력된 이미지
    """
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