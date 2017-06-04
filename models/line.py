import cv2
import math

from utils.logging_ import logger


X = 0
Y = 1

class Line():
    def __init__(self, st, ed, lim=(1920,1080)) -> None:
        super().__init__()
        if not(type(st) is tuple and type(ed) is tuple):
            raise ValueError("Invalid Argument")
        if not(len(st) == 2 and len(ed) == 2):
            raise ValueError("Invalid Argument")
        self.st = st
        self.ed = ed
        if self.x1 > self.x2:
            temp = self.st
            self.st = self.ed
            self.ed = temp
        elif self.x1 == self.x2:
            if self.y1 > self.y2:
                temp = self.st
                self.st = self.ed
                self.ed = temp
        self.curpoint = self.st
        self.lim = lim

    @classmethod
    def drawLines(cls, image, lines, color=(0, 0, 255)):
        img = image[:]
        for line in lines:
            x1, y1, x2, y2 = line[0]
            logger.debug("drawLines x1,y1,x2,y2={},{},{},{}".format(x1, y1, x2, y2))
            cv2.line(img, (x1, y1), (x2, y2), color, 2)

        return img

    @property
    def baseorigin(self):
        def _isValidAxis(point, lim):
            x, y = point[X], point[Y]
            xlim, ylim = lim[X], lim[Y]

            result = True
            if not (x >= 0 and x < xlim):
                result = False
            if not (y >= 0 and y < ylim):
                result = False
            return result

        while True:
            prevpoint = self.prevpoint_asint
            logger.debug("prevpoint={}".format(prevpoint))
            logger.debug("curpoint={}".format(self.curpoint))
            if not _isValidAxis(prevpoint, self.lim):
                break

        nextpoint = self.nextpoint_asint
        logger.debug("prevpoint={}".format(nextpoint))
        logger.debug("curpoint={}".format(self.curpoint))
        return nextpoint


    @property
    def prevpoint(self):
        direction = self.direction
        self.curpoint = (self.curpoint[X] - direction[X],
                        self.curpoint[Y] - direction[Y])
        return self.curpoint

    @property
    def prevpoint_asint(self):
        point = self.prevpoint
        return self.asint(point)

    def asint(self, point):
        return (round(point[X]), round(point[Y]))

    @property
    def nextpoint(self):
        direction = self.direction
        self.curpoint = (self.curpoint[X] + direction[X],
                        self.curpoint[Y] + direction[Y])
        return self.curpoint

    @property
    def nextpoint_asint(self):
        point = self.nextpoint
        return self.asint(point)

    @property
    def direction(self):
        deltax = self.ed[X] - self.st[X]
        deltay = self.ed[Y] - self.st[Y]

        if deltax == 0:
            direction = (0, deltay)
        else:
            if abs(deltax) > abs(deltay):
                direction = (1, deltay / deltax)
            else:
                direction = (deltax / deltay, 1)

        logger.debug("direction={}".format(direction))
        return direction

    @property
    def cos(self):
        deltax, deltay = self.x2 - self.x1, self.y2 - self.y1
        length = (deltax ** 2 + deltay ** 2) ** (1 / 2)
        cos = deltax / length
        return cos

    @property
    def x1(self):
        return self.st[X]

    @property
    def x2(self):
        return self.ed[X]

    @property
    def y1(self):
        return self.st[Y]

    @property
    def y2(self):
        return self.ed[Y]

    @property
    def sin(self):
        deltax, deltay = self.x2 - self.x1, self.y2 - self.y1
        length = (deltax ** 2 + deltay ** 2) ** (1 / 2)
        sin = deltay / length
        return sin

    @property
    def radian(self):
        radian = math.asin(self.sin)
        return radian

    @property
    def degree(self):
        degree = math.degrees(self.radian)
        return degree