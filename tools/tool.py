import cv2
import numpy as np


def imshow_(img):
    cv2.imshow('processing', img)
    cv2.waitKey(0)


def randomcolor():
    import random
    import math
    r = math.floor(random.random() * 255)
    g = math.floor(random.random() * 255)
    b = math.floor(random.random() * 255)

    return (r, g, b)


def drawcontour(rgb, gray):
    img2, contours, hierarchy = cv2.findContours(gray.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        aspectratio = float(w) / h
        height, width = gray.shape
        pick_area = w * h
        total_area = width * height
        # extent = float(pick_area) / total_area
        extent = float(area) / total_area

        # if len(approx) == 4 and (extent) > 0.005:
        if extent > 0.005:
            cv2.drawContours(rgb, [c], -1, randomcolor(), 2)
            # imshow_(img)


def gradient(img):
    img_x = cv2.Sobel(img, -1, 1, 0)
    # img_xy = img_x
    img_y = cv2.Sobel(img, -1, 0, 1)
    img_xy = np.power((np.power(img_x, 2) + np.power(img_y, 2)), 1 / 2)
    img_xy = cv2.normalize(img_xy.astype('uint8'), None, 0, 255, cv2.NORM_MINMAX)
    return img_xy


def threshold(img, threshold=0.65):
    img_histeq = cv2.equalizeHist(img)
    return np.multiply(img, img_histeq > 255 * threshold)


def lsd(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lsd = cv2.createLineSegmentDetector()
    mask = np.ones(img.shape)
    lines = lsd.detect(img, mask)

    for line in lines[0]:
        [x1, y1, x2, y2] = line[0]
        cv2.line(mask, (x1, y1), (x2, y2), randomcolor(), 1)

    return mask


def matcher(img1, img2):
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 10 matches.
    img3 = np.zeros(img1.shape)
    return cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], img3, flags=2)