import cv2

from logics.feature.corner_detector import detectCornerWithFAST
from logics.feature.gradient_detector import gradienty, canny, gradientx
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
        mask = gradientx(image)

    elif method == "gradienty":
        mask = gradienty(image)
        # overwrite = canny(image)
        # mask = canny(image)

    return mask, overwrite, mainline

def convertFeatureMaps(image):
    features = []
    mask, overwrite, _ = convertFeatureMap(image, 'gradienty')
    features.append(mask)

    mask, overwrite, _ = convertFeatureMap(image, 'canny')
    features.append(mask)

    mask, overwrite, _ = convertFeatureMap(image, 'fast')
    features.append(mask)

    return features