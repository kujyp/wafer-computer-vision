import cv2
import operator

import numpy as np
import time

from logics.middleware.featuremap_converter import convertFeatureMap
from logics.region.InterestRegionFinder import region_of_interest
from models.line import Line, X, Y
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
    # WindowManager.getInstance().imgshow(color, '2')
    cv2.waitKey(1000)
    for i in range(NUMOFCONTOURLINES):
        st = st+i
        ed = st+1
        _lines = contourLines[st:ed]
        color = Line.drawLines(color, _lines)
        # WindowManager.getInstance().imgshow(color, '2')
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



# 0610

def findContour(img):
    copy = np.copy(img)
    # 범위두고 많은곳 고르기
    length = copy.shape
    if len(length) == 3:
        color = copy
        copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    else:
        color = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)

    xlen, ylen = length[1], length[0]
    yst, yed = 0, ylen
    NDIV = 10
    xdiv = xlen / NDIV
    sumdict = dict()

    for i in range(NDIV):
        xst, xed = int(i * xdiv), int((i+1) * xdiv)
        div = copy[yst:yed, xst:xed]
        sum_ = np.sum(div)
        # logger.debug("div.shape={}, divsum={}".format(div.shape, sum_))
        key = (xst, xed)
        sumdict[key] = sum_


    sortedsum = sorted(sumdict.items(), reverse=True, key=operator.itemgetter(1))

    NRESULT = 2
    masked = None
    # logger.debug("findContour result")
    for item in sortedsum[0:NRESULT]:
        xst, xed = item[0]
        sum_ = item[1]
        # logger.debug("xst, xed={},{}, divsum={}".format(xst, xed, sum_))

        vertices = np.array([[(xst, yst), (xed, yst), (xed, yed), (xst, yed)]], dtype=np.int32)
        masked = region_of_interest(copy, vertices)
        cv2.rectangle(color, (xst,yst), (xed,yed), (0,255,0), 3)
        cv2.putText(color,"xst,yst={},{}".format(xst,yst),(xed+10,yst+50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
        cv2.putText(color, "xed,yed={},{}".format(xed, yed), (xed + 10, yst + 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
        # cv2.drawContours(color, [(xst, yst), (xed, yst), (xed, yed), (xst, yed)], 3, (0,255,0), 3)

    return color

def findContourWithFixedRange(image, rng):
    copy = np.copy(image)
    length = copy.shape
    if len(length) != 3:
        copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)

    xst, xed = rng[0], rng[2]
    yst, yed = rng[1], rng[3]
    cv2.rectangle(copy, (xst, yst), (xed, yed), (0, 255, 0), 3)
    cv2.putText(copy, "xst,yst={},{}".format(xst, yst), (xed + 10, yst + 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(copy, "xed,yed={},{}".format(xed, yed), (xed + 10, yst + 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)

    return copy

def findContourWithCv2(img):
    # findCountour활용하기
    copy = np.copy(img)
    length = copy.shape
    if len(length) == 3:
        color = copy
        copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    else:
        color = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)

    mask = np.zeros(color.shape)

    # ret, thresh = cv2.threshold(gray, 127, 255, 0)

    # ----------------------------------- WATER_SHED -----------------------------------
    ret, thresh = cv2.threshold(copy, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    ret, markers = cv2.connectedComponents(opening)

    markers = cv2.watershed(color, markers)

    mask[markers == -1] = [255, 0, 0]
    # ----------------------------------- WATER_SHED -----------------------------------

    # ----------------------------------- ACTIVE_CONTOUR -----------------------------------
    # from skimage.segmentation import active_contour
    # from skimage.filters import gaussian
    #
    # xst, xed = 830, 1150  # Video4
    # yst, yed = 0, length[0]

    # x = np.concatenate((np.linspace(xst, xed, 50),
    #     np.linspace(xed, xed, 50),
    #     np.linspace(xed, xst, 50),
    #     np.linspace(xst, xst, 50)), axis=0)
    # y = np.concatenate((np.linspace(yst, yst, 50),
    #     np.linspace(yst, yed, 50),
    #     np.linspace(yed, yed, 50),
    #     np.linspace(yed, yst, 50)), axis=0)
    # init = np.array([x, y]).T
    #
    # snake = active_contour(copy,
    #                        init, w_edge=2)
    # # im2, contours, hierachy = cv2.findContours(copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # # cv2.drawContours(mask, contours, -1, (0,255,0), 1)
    #
    # import matplotlib.pyplot as plt
    # fig = plt.figure(figsize=(7, 7))
    # ax = fig.add_subplot(111)
    # plt.gray()
    # ax.imshow(img)
    # ax.plot(init [:, 0], init [:, 1], '--r', lw=3)
    # ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
    # ax.set_xticks([]), ax.set_yticks([])
    # ax.axis([0, img.shape[1], img.shape[0], 0])
    # ----------------------------------- ACTIVE_CONTOUR -----------------------------------

    return mask
