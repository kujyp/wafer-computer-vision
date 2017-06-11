import cv2
import time

import numpy as np

from logics.contour.contour_detector import detectContour, findContour, findContourWithCv2, findContourWithFixedRange
from logics.middleware.featuremap_converter import convertFeatureMap, convertFeatureMaps
from logics.region.InterestRegionFinder import findInterestRegion
from models.line import Line
from utils.visualize.videoloader import VideoLoader
from utils.visualize.windowmanager import WindowManager, NUMOFCOLS

video = VideoLoader.getInstance()
video.load(4) # 4 : ch01 normal ch1
windowManager = WindowManager.getInstance()
windowManager.addWindow(['UP_1',
                         'UP_2',
                         'UP_3',
                         'UP_4',
                         'DOWN_1',
                         'DOWN_2',
                         'DOWN_3',
                         'DOWN_4'])

a = Line((20,15), (40,20))
mask = np.zeros((1080,1920,3))
# shape=(1080, 1920, 3)
Line.drawLines(mask, a.baseline)
# windowManager.imgshow(mask, 'original')

while True:
    frame = video.next()
    if frame is None:
        break

    windowManager.imgshow(frame, 'UP_1')

    interest, cropped, rng= findInterestRegion(frame)
    interest_contour = findContourWithFixedRange(interest, rng)
    # interest_contour = findContourWithCv2(interest)
    windowManager.imgshow(interest_contour, 'DOWN_1')

    features = convertFeatureMaps(interest)
    for idx, feature in enumerate(features):
        windowManager.imgshow(feature, 1+idx)

    contours = []
    for feature in features:
        # contours.append(findContourWithCv2(feature))
        contours.append(findContourWithFixedRange(feature, rng))
        # contours.append(findContour(feature))

    for idx, contour in enumerate(contours):
        windowManager.imgshow(contour, 1+NUMOFCOLS+idx)

    # feature, _, mainline = convertFeatureMap(canny_, 'hough')
    # windowManager.imgshow(feature, 'DOWN_1')
    # feature, _, mainline = convertFeatureMap(fast_, 'hough')
    # windowManager.imgshow(feature, 'DOWN_2')
    # feature, _, mainline = convertFeatureMap(gradient_, 'hough')
    # windowManager.imgshow(feature, 'DOWN_4')

    # feature = detectContour(frame)

    # windowManager.imgshow(overwrite, '3')
    # windowManager.imgshow(mainlineboundary, '4')
    # subtracked = subtractBackground(frame)
    # windowManager.imgshow(subtracked, 'subtracked')
    # corner = detectCornerWithFAST(frame)
    # windowManager.imgshow(corner, 'corner')
    # corner = detectCornerWithShiTomasi(frame)
    # corner = detectCornerWithHarris(frame)
    # windowManager.imgshow(corner, 'surf')
    # contour = detectContourLine(frame)
    # windowManager.imgshow(contour, 'contourvideo')


    second = 1
    time.sleep(second)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()