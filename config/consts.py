# status
class Status:
    NORMAL = 0
    LEFT_ABNORMAL = 1
    RIGHT_ABNORMAL = 2

class InNumpyarray:
    X = 1
    Y = 0

class Color:
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)

class DelayTypes:
    TIME = 0
    KEYBOARDINTERRUPT = 1

class FeatureMethod:
    Gradient = "gradient"
    GradientY = "gradienty"
    GradientX = "gradientx"
    Fast = "fast"
    Canny = "canny"