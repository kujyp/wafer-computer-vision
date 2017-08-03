import cv2

import time

from config import config
from config.consts import *
from logics.contour.contour_detector import findContourWithFixedRange
from logics.middleware.featuremap_converter import convertFeatureMaps
from logics.region.region_detector import detect_target_region
from logics.regist.TemplateRegister import finddelta_withtemplate, drawNormalRectangle, deltaStatus, finddelta
from models.calibration import Calibration
from utils.visualize.sourceloader import SourceLoader
from utils.visualize.videoloader import VideoLoader
from utils.visualize.windowmanager import WindowManager


# 초기화
source = SourceLoader.getSource()
window_manager = WindowManager.getInstance()
calibration = Calibration.getInstance()

# Calibration 안된경우에 Calibration 진행
if calibration.isLoaded():
    print("Calibration Loaded")
else:
    raise("Need to calibration")

# 영상처리
while True:
    origin = source.next()
    if origin is None:
        break

    # 기둥 있는 영역 감지
    detected, cropped = detect_target_region(origin)
    window_manager.imgshow(origin, 0)
    window_manager.imgshow(detected, 1)
    window_manager.showWindows()

    # 정상과의 차이 감지
    delta = finddelta(detected)
    # draw
    # show

    # 정상/비정상 판단
    status = deltaStatus(delta)
    if status == Status.RIGHT_ABNORMAL:
        pass
    elif status == Status.LEFT_ABNORMAL:
        pass
    elif status == Status.NORMAL:
        pass
    # draw
    # show

    # 딜레이
    if config.DELAY_TYPE == DelayTypes.TIME:
        cv2.waitKey(config.DELAY_TIME_INMILLIS)
    elif config.DELAY_TYPE == DelayTypes.KEYBOARDINTERRUPT:
        cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()