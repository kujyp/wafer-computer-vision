import cv2
import time

from src_0602.ContourLineDetector import detectContourLine
from src_0602.VideoLoader import VideoLoader

from logics.CornerDetector import detectCornerWithFAST
from utils.visualize.WindowManager import WindowManager

video = VideoLoader.getInstance()
windowManager = WindowManager.getInstance()
windowManager.addWindow(['original',
                         'corner',
                         'surf',
                         'contourvideo'])


while True:
    frame = video.next()
    if frame is None:
        break

    windowManager.imgshow(frame, 'original')
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