
# contour_detector 아래 지운파일
MINIMUM_POINTS_FOR_LINE = 3
NUM_OF_DIRECTIONS = 2000
INF = 100000
# VIDEO_RESOLUTION = {
#     'y':1080,
#     'x':1920,
#     'color':3
# }
HORIZONTAL_DIRACTION = (1.0, 0.0)
# LINE_LIMITLENGTH = VIDEO_RESOLUTION['x'] / 40


# contour_detector 하지만 안사용중
NUMOFCONTOURLINES = 400

# status
class Status:
    NORMAL = 0
    LEFT_ABNORMAL = 1
    RIGHT_ABNORMAL = 2

class Video_resolution:
        resolution_y = 1080
        resolution_x = 1920
        resolution_colordim = 3

class Line_config:
    X = 0
    Y = 1
    LIMIT_BOUNDARY = (10 / 1920)
    LINE_BOUNDARY_RANGE = int(Video_resolution.resolution_x * (250.0 / 1920.0))

class color:
    pass

class MediaTypes:
    VIDEO = 0
    PHOTO = 1

class DelayTypes:
    TIME = 0
    KEYBOARDINTERRUPT = 1