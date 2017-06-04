import cv2

import numpy as np

from utils.Logger import logger


def detectCornerWithFAST(image):
    img = image[:]
    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # Print all default params
    logger.debug("Threshold: {}".format(fast.getThreshold()))
    logger.debug("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
    logger.debug("neighborhood: {}".format(fast.getType()))
    logger.debug("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    logger.debug("Total Keypoints without nonmaxSuppression: {}".format(len(kp)))
    img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # return img2
    return img3

def detectCornerWithShiTomasi(image):
    img = image[:]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, 255, 3)
    return img

def detectCornerWithHarris(image):
    img = image[:]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # find Harris corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    # Now draw them
    logger.debug("centroids={}, corners={}".format(len(centroids), len(corners)))
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    img[res[:, 1], res[:, 0]] = [0, 0, 255]
    img[res[:, 3], res[:, 2]] = [0, 255, 0]

    return img