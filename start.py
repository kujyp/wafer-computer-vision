import cv2

from config import config
from config.consts import *
from logics.drawer.status_visualizer import show_calibrated_rectangle, show_statusmessage
from logics.region.region_detector import detect_target_region
from logics.region.template_register import delta_status, finddelta
from utils.calibration.calibration import Calibration
from utils.log.logging_ import logger
from utils.visualize.videoloader import VideoLoader
from utils.visualize.windowmanager import WindowManager

# 초기화
source = VideoLoader.getInstance()
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
    detected, cropped, position = detect_target_region(origin)
    window_manager.imgshow(origin, 0)
    window_manager.imgshow(detected, 1)
    window_manager.showWindows()

    # 정상과의 차이 감지
    delta = finddelta(detected)
    withcalibratedrectangle = show_calibrated_rectangle(detected, delta)
    segmentedwithrectangle = show_calibrated_rectangle(detected, delta)
    window_manager.imgshow(segmentedwithrectangle, 2)
    logger.info("delta={}".format(delta))

    # 정상/비정상 판단
    status = delta_status(delta)

    result_msg = ""
    if status == Status.RIGHT_ABNORMAL:
        result_msg = Messages.ON_RIGHT_ABNORMAL
    elif status == Status.LEFT_ABNORMAL:
        result_msg = Messages.ON_LEFT_ABNORMAL
    elif status == Status.NORMAL:
        result_msg = Messages.ON_NORMAL

    withstatusmessage = show_statusmessage(withcalibratedrectangle, result_msg=result_msg, position=position, color=Color.RED)
    window_manager.imgshow(withstatusmessage, 3)
    logger.info("result={}".format(result_msg))

    # 딜레이
    if config.DELAY_TYPE == DelayTypes.TIME:
        cv2.waitKey(config.DELAY_TIME_INMILLIS)
    elif config.DELAY_TYPE == DelayTypes.KEYBOARDINTERRUPT:
        cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()