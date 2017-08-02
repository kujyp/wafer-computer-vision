from config.consts import *


class Source:
    # 입력 미디어 타입 : 비디오 / 사진
    INPUT_MEDIA_TYPE = MediaTypes.VIDEO
    # INPUT_MEDIA_TYPE = MediaTypes.PHOTO

    CALIBRATION_CROPPED_TEMPLATE_PATH = "data/calibration/cropped_template.png"

    VIDEO_SOURCE_DIRECTORY = "data/sources/"
    # VIDEO_SOURCE_FILENAME 비워두면 폴더내에서 랜덤하게 고름
    # VIDEO_SOURCE_FILENAME = ""
    VIDEO_SOURCE_FILENAME = "ch01 Lup ch1.mpg"

# 사진한장 처리후 딜레이타입
DELAY_TYPE = DelayTypes.TIME
DELAY_TIME_INSECONDS = 0.5
# DELAY_TYPE = DelayTypes.KEYBOARDINTERRUPT


class Textdimens:
    TEXT_X_MARGIN = 50
    TEXT_FONTSIZE = 1.5
    TEXT_LINEWIDTH = 3
    TEXT_LINESPACING = 50
    TEXT_TOPLINESPACING = 100
