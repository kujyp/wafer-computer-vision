import cv2

from src_0602.Logger import logger


def detectCorner(image):
    img = image[:]
    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # Print all default params
    logger.debug("Threshold: {}".format(fast.getThreshold()))
    logger.debug("nonmaxSuppression: {}".format(fast.getNonmaxSuppression()))
    logger.debug("neighborhood: ".format(fast.getType()))
    logger.debug("Total Keypoints with nonmaxSuppression: ".format(len(kp)))
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    logger.debug("Total Keypoints without nonmaxSuppression: ".format(len(kp)))
    img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # return img2
    return img3