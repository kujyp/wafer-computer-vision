import cv2
import os

import time

from src_0602.BackgroundSubtractor import subtractBackground
from src_0602.ContourLineDetector import detectContourLine
from src_0602.Imshower import imgshow

video_dir = "data/mpg인코딩"
video_filename = 'ch01 Lup ch1.mpg'
# video_filename = 'KakaoTalk_Video_2017-03-03-14-41-55 (1).mp4'
video_filename = os.path.join(video_dir, video_filename)

alive_flag = False
if alive_flag:
    video_capture = cv2.VideoCapture(0)
else:
    video_capture = cv2.VideoCapture(video_filename)

NUM_PRELOAD_FRAMES = 10
loaded_frame = []
loaded_frame.extend(range(NUM_PRELOAD_FRAMES))

# if True:
terminate = False
cv2.namedWindow('subtracked', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('contourvideo', cv2.WINDOW_KEEPRATIO)
width = 959
height = 1000
cv2.resizeWindow('subtracked', width, height)
cv2.resizeWindow('contourvideo', width, height)
cv2.moveWindow('subtracked', 0,0)
cv2.moveWindow('contourvideo', width, 0)

while True:
    for i in range(NUM_PRELOAD_FRAMES):
        _, loaded_frame[i] = video_capture.read()
        if loaded_frame[i] is None:
            terminate = True

    if terminate:
        break

    frame = loaded_frame[0]
    subtracked = subtractBackground(frame)
    contour = detectContourLine(frame)


    imgshow(subtracked, 'subtracked',(width,height))
    imgshow(contour, 'contourvideo',(width,height))

    second = 1
    time.sleep(second)

    # if True:
    #     cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()