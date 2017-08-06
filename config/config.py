from config.consts import *


class Source:
    CALIBRATION_PATH = "data/calibration/"

    # CALIBRATION_TEMPLATE_FILENAME = 정상위치 전체 사진
    CALIBRATION_TEMPLATE_FILENAME = "sample_template.png"
    CALIBRATION_TEMPLATE_PATH = CALIBRATION_PATH + CALIBRATION_TEMPLATE_FILENAME

    # CALIBRATION_CROPPED_TEMPLATE_FILENAME = 정상위치 기둥 잘라낸 사진
    CALIBRATION_CROPPED_TEMPLATE_FILENAME = "sample_template_cropped.png"
    # CALIBRATION_CROPPED_TEMPLATE_FILENAME  = "cropped_template.png"
    CALIBRATION_CROPPED_TEMPLATE_PATH = CALIBRATION_PATH + CALIBRATION_CROPPED_TEMPLATE_FILENAME

    # 위의 두 파일로 생성하는 파일
    CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_FILENAME = "sample_template_croppedposition_inpixel.npy"
    # CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_FILENAME = "cropped_templateposition_inpixel.npy"
    CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_PATH = CALIBRATION_PATH + CALIBRATION_CROPPED_TEMPLATEPOSITION_INPIXEL_FILENAME

    XEND = 'xend'
    XSTART= 'xstart'

    # 데이터 폴더
    VIDEO_SOURCE_DIRECTORY = "data/sources/"

    # VIDEO_SOURCE_FILENAME 비워두면 폴더내에서 랜덤하게 고름
    # VIDEO_SOURCE_FILENAME = ""
    VIDEO_SOURCE_FILENAME = "ch01 Lup ch1.mpg"

    # VIDEO_NUM_SKIP_FRAMES 한장처리후 스킵하는 FRAME수 컴퓨터 성능에 따라 조정 필요없을시 0
    VIDEO_NUM_SKIP_FRAMES = 30

class VideoResolution:
    # 비디오의 해상도
    RESOLUTION_Y = 1080
    RESOLUTION_X = 1920
    RESOLUTION_COLORDIM = 3


class Window:
    # 모니터링 윈도우 이름
    WINDOWNAMES = [
        "Original",
        "Window2",
        "Window3",
        "Window4",

        "Window5",
        "Window6",
        "Window7",
        "Window8"
    ]

    # 모니터링 윈도우 개수 가로/세로
    NUMOF_WINDOW_COLUMNS = 4
    NUMOF_WINDOW_ROWS = 1
    # FULL_SCREEN_WIDTH = 1000
    # FULL_SCREEN_HEIGHT = 950

    # 모니터링 화면전체 픽셀수
    FULL_SCREEN_WIDTH = 959 * 2
    FULL_SCREEN_HEIGHT = 1000
    FIXED_BAR_HEIGHT = 40

class StatusThreshold:
    # 몇픽셀까지 정상으로 할것인지
    THRESHOLD_IN_PIXEL = 20

# 사진한장 처리후 딜레이타입 / 동영상 처리중에 cv2.imshow()를 위해서 멈출 필요 있음
class Delay:
    DELAY_TYPE = DelayTypes.TIME
    DELAY_TIME_INMILLIS = 500
    # DELAY_TYPE = DelayTypes.KEYBOARDINTERRUPT

# 사진 위에 그려지는 글자들 크기 등 설정
class Textdimens:
    TEXT_X_MARGIN = 50
    TEXT_FONTSIZE = 1.5
    TEXT_LINEWIDTH = 3
    TEXT_LINESPACING = 50
    TEXT_TOPLINESPACING = 100

# 사진 위에 그려지는 메세지
class Messages:
    ON_RIGHT_ABNORMAL = "Out of range(RIGHT)"
    ON_LEFT_ABNORMAL = "Out of range(LEFT)"
    ON_NORMAL = "On Normal range."
