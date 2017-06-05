import cv2

import numpy as np


def detectContour(image):
    img = np.copy(image)
    color = img
    if len(img.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        gray = img
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    gray, contours, hierarchy = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # peri = cv2.arcLength(c, True)
        # approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # area = cv2.contourArea(c)
        # x, y, w, h = cv2.boundingRect(c)
        # aspectratio = float(w) / h
        # height, width = gray.shape
        # pick_area = w * h
        # total_area = width * height
        # extent = float(pick_area) / total_area
        # extent = float(area) / total_area

        # if len(approx) == 4 and (extent) > 0.005:
        # if extent > 0.005:
        cv2.drawContours(color, [c], -1, (0,0,255), 2)
        pass
            # imshow_(img)
    return color