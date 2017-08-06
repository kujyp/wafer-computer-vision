import cv2

from config.config import StatusThreshold, Source
from config.consts import Status
from utils.calibration.calibration import Calibration


def regist(image, template):
    """
    이미지 둘을 매칭시켜 매칭시킨 위치의 X좌표를 반환
    
    :param image: 원본 이미지
    :param template: 매칭시킬 Template 이미지
    :return: 두 이미지의 매칭 된 위치의 X좌표 
    """

    meth = 'cv2.TM_CCOEFF_NORMED'
    clone = image.copy()

    method = eval(meth)
    res = cv2.matchTemplate(clone, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    return top_left[0]

def find_delta(img):
    """
    기둥의 위치를 찾아서 정상 사진과 X좌표 차이를 반환
    
    :param img: 원본이미지 
    :return: 정상 사진과 X좌표 차이
    """
    return regist(img, Calibration.getInstance().CROPPED_TEMPLATE) - \
           Calibration.getInstance().CROPPED_TEMPLATEPOSITION_INPIXEL[Source.XSTART]

def delta_status(delta):
    """
    기둥의 위치가 정상 범위인지 판단
    
    :param delta: 기둥이 시작되는 X위치
    :return: Status 값 반환 NORMAL, RIGHT_ABNORMAL, LEFT_ABNORMAL
    """
    if delta > StatusThreshold.THRESHOLD_IN_PIXEL:
        return Status.RIGHT_ABNORMAL
    elif delta < -StatusThreshold.THRESHOLD_IN_PIXEL:
        return Status.LEFT_ABNORMAL

    return Status.NORMAL
