import cv2
import math

import numpy as np

from config.consts import Video_resolution, Line_config
from utils.log.logging_ import logger


class Line():
    def __init__(self, st, ed,
                 lim=(Video_resolution.resolution_x, Video_resolution.resolution_y)) -> None:
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
        self._baseorigin = None
        self._basedest = None
        self._direction = None
        self._length = None

    @classmethod
    def getBaseLineWeight(cls, image, line):
        point_iter = line.getBasePoints
        weight = 0

        for point in point_iter:
            x, y = int(point[X]), int(point[Y])
            weight += image[y,x]
            # logger.debug("axis={}, point={}".format((x,y), image[x,y]))

        # logger.debug("weight={}".format(weight))
        return weight

    @property
    def getBasePoints(self):
        basePoints = []
        self.curpoint = self.baseorigin
        while True:
            nextpoint = self.nextpoint_asint
            # logger.debug("prevpoint={}".format(prevpoint))
            # logger.debug("curpoint={}".format(self.curpoint))
            if not self._isValidAxis(nextpoint, self.lim):
                break
            basePoints.append(nextpoint)

        return basePoints

    @property
    def boundaryLines(self):
        lines = []
        (x1, y1) = self.baseorigin
        (x2, y2) = self.basedest
        if self.direction == (1.0, 0.0):
            logger.warn("boundaryLines/direction is horizontal")
            pass
        else:
            for iter in [Line_config.LINE_BOUNDARY_RANGE, -Line_config.LINE_BOUNDARY_RANGE]:
                step = int(iter/abs(iter))
                for i in range(0, iter, step):
                    if step == -1 and i == 0:
                        continue
                    xp1 = x1+i
                    xp2 = x2+i
                    if self.isBoundary((xp1, 0)):
                        break
                    st = (xp1, y1)
                    ed = (xp2, y2)
                    lines.append(Line(st,ed))

        return lines

    @classmethod
    def drawLines(cls, image, lines, color=(0, 0, 255)):
        # img = np.copy(image)
        img = np.copy(image)
        for line in lines:
            if type(line) == Line:
                ori, dst = line.baseorigin, line.basedest
            else:
                if len(line) == 1:
                    line = line[0]
                x1, y1, x2, y2 = line
                ori, dst = (x1, y1), (x2, y2)
            # logger.debug("drawLines x1,y1,x2,y2={},{},{},{}".format(x1, y1, x2, y2))
            ori, dst = (int(ori[X]), int(ori[Y])), (int(dst[X]), int(dst[Y]))
            cv2.line(img, ori, dst, color, 2)

        return img

    def isBoundary(self, axis=None):
        if axis is None:
            axis = self.baseorigin

        if (axis[X] > (self.lim[X] -
                           (self.lim[X] * LIMIT_BOUNDARY))) or (
                    axis[X] < (self.lim[X] * LIMIT_BOUNDARY)):
            return True
        # if (self.baseorigin[Y] > (self.lim[Y] -
        #                                   (self.lim[Y] * LIMIT_BOUNDARY))) or (
        #                 self.baseorigin[Y] < (self.lim[Y] * LIMIT_BOUNDARY)):
        #     return True
        return False

    @property
    def baseorigin(self):
        if self._baseorigin is None:
            while True:
                prevpoint = self.prevpoint_asint
                # logger.debug("prevpoint={}".format(prevpoint))
                # logger.debug("curpoint={}".format(self.curpoint))
                if not self._isValidAxis(prevpoint, self.lim):
                    break

            nextpoint = self.nextpoint_asint
            # logger.debug("nextpoint={}".format(nextpoint))
            # logger.debug("curpoint={}".format(self.curpoint))
            self._baseorigin = nextpoint

        return self._baseorigin

    def _isValidAxis(self, point, lim):
        x, y = point[X], point[Y]
        xlim, ylim = lim[X], lim[Y]

        result = True
        if not (x >= 0 and x < xlim):
            result = False
        if not (y >= 0 and y < ylim):
            result = False
        return result

    @property
    def baseline(self):
        x1, y1 = self.baseorigin
        x2, y2 = self.basedest
        return [(x1,y1,x2,y2)]

    @property
    def basedest(self):
        if self._basedest is None:
            while True:
                nextpoint = self.nextpoint_asint
                # logger.debug("nextpoint={}".format(nextpoint))
                # logger.debug("curpoint={}".format(self.curpoint))
                if not self._isValidAxis(nextpoint, self.lim):
                    break

            prevpoint = self.prevpoint_asint
            # logger.debug("prevpoint={}".format(prevpoint ))
            # logger.debug("curpoint={}".format(self.curpoint))
            self._basedest = prevpoint

        return self._basedest

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
        if self._direction is None:
            deltax = self.ed[X] - self.st[X]
            deltay = self.ed[Y] - self.st[Y]

            if deltax == 0:
                direction = (0.0, 1.0)
            else:
                if abs(deltax) > abs(deltay):
                    direction = (1.0, deltay / deltax)
                else:
                    direction = (deltax / deltay, 1.0)

            # logger.debug("direction={}".format(direction))
            self._direction = direction
        return self._direction

    @property
    def cos(self):
        deltax = self.x2 - self.x1
        cos = deltax / self.length
        return cos

    @property
    def length(self):
        if self._length is None:
            deltax, deltay = self.x2 - self.x1, self.y2 - self.y1
            self._length = (deltax ** 2 + deltay ** 2) ** (1 / 2)

        return self._length

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