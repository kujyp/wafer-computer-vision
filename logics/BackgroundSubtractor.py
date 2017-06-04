import cv2

import numpy as np

from utils.Logger import logger


def subtractBackground(img):
    clone = img
    mask = np.zeros(clone.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    logger.info(clone.shape)
    rect = (900, 0, 400, 1080)
    cv2.grabCut(clone, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    color = (255,0,0)
    cv2.rectangle(clone,(rect[0], rect[1]), (rect[2], rect[3]), color, 5)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    clone = clone * mask2[:, :, np.newaxis]

    return clone