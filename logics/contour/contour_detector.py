import cv2
import operator

import numpy as np
import time

from logics.middleware.featuremap_converter import convertFeatureMap
from models.line import Line
from utils.logging_ import logger
from utils.visualize.windowmanager import WindowManager

NUMOFCONTOURLINES = 400

def detectContour(image):
    img = np.copy(image)
    color = img
    if len(img.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        gray = img

    _, _, mainline = convertFeatureMap(img, 'hough')
    feature, overwrite, _ = convertFeatureMap(img, 'canny')

    contourLines = getContourLines(feature, mainline)

    st = 0
    WindowManager.getInstance().imgshow(color, '2')
    cv2.waitKey(1000)
    for i in range(NUMOFCONTOURLINES):
        st = st+i
        ed = st+1
        _lines = contourLines[st:ed]
        color = Line.drawLines(color, _lines)
        WindowManager.getInstance().imgshow(color, '2')
        second = 0.05
        millis = int(second*1000)
        cv2.waitKey(millis)
        # second = 1
        # time.sleep(second)
        logger.debug("Draw contourLine {} times".format(i))

    return color

def getContourLines(img, mainline):
    feature = np.copy(img)
    if len(feature.shape) == 3:
        feature = cv2.cvtColor(feature, cv2.COLOR_BGR2GRAY)

    boundaryLines = mainline.boundaryLines

    weightdict = dict()
    for line in boundaryLines:
        weight = Line.getBaseLineWeight(feature, line)
        weightdict[line] = weight

    sorteddict = sorted(weightdict.items(), key=operator.itemgetter(1))
    contourLines = []
    numlines = min(NUMOFCONTOURLINES, len(sorteddict))
    for item in sorteddict[-1:(-1 - numlines):-1]:
        contourLines.append(item[0])

    return contourLines