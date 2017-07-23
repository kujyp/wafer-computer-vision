import cv2
import numpy as np
from config.config import Textdimens


def findContourWithFixedRange(image, rng):
    copy = np.copy(image)
    length = copy.shape
    if len(length) != 3:
        copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)

    xst, xed = rng[0], rng[2]
    yst, yed = rng[1], rng[3]
    cv2.rectangle(copy, (xst, yst), (xed, yed), (0, 255, 0), 3)
    cv2.putText(copy, "Current", (xed + Textdimens.TEXT_X_MARGIN, yst + 50),
                cv2.FONT_HERSHEY_SIMPLEX, Textdimens.TEXT_FONTSIZE, (0, 255, 0), Textdimens.TEXT_LINEWIDTH, cv2.LINE_AA)
    cv2.putText(copy, "x=[{}-{}]".format(xst, xed), (xed + Textdimens.TEXT_X_MARGIN, yst + 100),
                cv2.FONT_HERSHEY_SIMPLEX, Textdimens.TEXT_FONTSIZE, (0, 255, 0), Textdimens.TEXT_LINEWIDTH, cv2.LINE_AA)

    return copy