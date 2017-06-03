import cv2
import os
import time

from src_0602.CornerDetector import detectCorner
from src_0602.WindowManager import WindowManager
from src_0602.BackgroundSubtractor import subtractBackground
from src_0602.ContourLineDetector import detectContourLine
from src_0602.VideoLoader import VideoLoader


video = VideoLoader.getInstance()
windowManager = WindowManager.getInstance()
windowManager.addWindow(['original',
                         'corner',
                         'contourvideo'])


while True:
    frame = video.next()
    if frame is None:
        break

    windowManager.imgshow(frame, 'original')
    # subtracked = subtractBackground(frame)
    # windowManager.imgshow(subtracked, 'subtracked')
    corner = detectCorner(frame)
    windowManager.imgshow(corner, 'corner')
    contour = detectContourLine(frame)
    windowManager.imgshow(contour, 'contourvideo')


    second = 1
    time.sleep(second)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()