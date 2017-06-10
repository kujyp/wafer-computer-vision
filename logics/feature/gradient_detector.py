import cv2

import numpy as np


def canny(img):
    return cv2.Canny(img, 10, 50)

def gradienty(img):
    img_y = cv2.Sobel(img,-1,1,0)
    # img_xy = np.power((np.power(img_x,2) + np.power(img_y,2)),1/2)
    # img_xy = cv2.normalize(img_xy.astype('uint8'), None, 0, 255, cv2.NORM_MINMAX)
    return img_y

def gradientx(img):
    img_x = cv2.Sobel(img,-1,0,1)
    return img_x
