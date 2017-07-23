import cv2

from logics.feature.corner_detector import detectCornerWithFAST
from logics.feature.gradient_detector import gradient_y, canny, gradient_x, gradient
from logics.feature.hough_line_detector import detectHoughLines


def convertFeatureMap(image, method="hough"):
    mask, overwrite, mainline = None, None, None
    if method == "hough":
        mask, overwrite, mainline = detectHoughLines(image)
    elif method == "fast":
        mask, overwrite, mainline = detectCornerWithFAST(image)
    elif method == "canny":
        # mask = gradient(image)
        # overwrite = canny(image)
        mask = canny(image)
    elif method == "gradientx":
        mask = gradient_x(image)

    elif method == "gradienty":
        mask = gradient_y(image)
    elif method == "gradient":
        mask = gradient(image)
        # overwrite = canny(image)
        # mask = canny(image)

    return mask, overwrite, mainline

def convertFeatureMaps(image):
    features = []
    mask, overwrite, _ = convertFeatureMap(image, 'gradient')
    features.append(mask)

    mask, overwrite, _ = convertFeatureMap(image, 'canny')
    features.append(mask)

    mask, overwrite, _ = convertFeatureMap(image, 'fast')
    features.append(mask)

    return features