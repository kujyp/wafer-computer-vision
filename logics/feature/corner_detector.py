import cv2
import numpy as np

from config.consts import Color


def detect_corner_with_fast(image):
    """
    FAST 알고리즘 적용하여 리턴합니다.
    
    :param image: 원본 이미지
    :return: mask: Feature Only 이미지, overwrite: Feature + Original 이미지 
    """

    img = np.copy(image)
    fast = cv2.FastFeatureDetector_create()
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    mask = np.zeros(img.shape, dtype=np.uint8)
    mask = cv2.drawKeypoints(mask, kp, None, color=Color.BLUE)
    overwrite = cv2.drawKeypoints(img, kp, None, color=Color.BLUE)

    return mask, overwrite