import cv2
import time

import numpy as np

from logics.contour_line_detector import detectContourLine
from logics.corner_detector import detectCornerWithFAST
from models.line import Line
from utils.logging_ import logger
from utils.visualize.videoloader import VideoLoader
from utils.visualize.windowmanager import WindowManager

video = VideoLoader.getInstance()
windowManager = WindowManager.getInstance()
windowManager.addWindow(['original',
                         'corner',
                         'surf',
                         'contourvideo'])

a = Line((20,15), (40,20))
mask = np.zeros((1080,1920,3))
# shape=(1080, 1920, 3)
Line.drawLines(mask, a.baseline)
windowManager.imgshow(mask, 'original')

while True:
    frame = video.next()
    if frame is None:
        break

    # windowManager.imgshow(frame, 'original')
    # subtracked = subtractBackground(frame)
    # windowManager.imgshow(subtracked, 'subtracked')
    corner = detectCornerWithFAST(frame)
    windowManager.imgshow(corner, 'corner')
    # corner = detectCornerWithShiTomasi(frame)
    # corner = detectCornerWithHarris(frame)
    # windowManager.imgshow(corner, 'surf')
    contour = detectContourLine(frame)
    windowManager.imgshow(contour, 'contourvideo')


    second = 1
    time.sleep(second)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()