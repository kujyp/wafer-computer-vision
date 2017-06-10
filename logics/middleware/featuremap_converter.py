import cv2

from logics.feature.corner_detector import detectCornerWithFAST
from logics.feature.gradient_detector import gradient, canny
from logics.feature.hough_line_detector import detectHoughLines


def convertFeatureMap(image, method="hough"):
    mask, overwrite, mainline = None, None, None
    if method == "hough":
        mask, overwrite, mainline = detectHoughLines(image)
    elif method == "fast":
        mask, overwrite, mainline = detectCornerWithFAST(image)
    elif method == "canny":
        mask = gradient(image)
        overwrite = canny(image)
        # mask = canny(image)

    return mask, overwrite, mainline