from logics.corner_detector import detectCornerWithFAST
from logics.hough_line_detector import detectHoughLines


def convertFeatureMap(image, method="hough"):
    mask, overwrite, mainline = None, None, None
    if method == "hough":
        mask, overwrite, mainline = detectHoughLines(image)
    elif method == "fast":
        mask, overwrite, mainline = detectCornerWithFAST(image)
    elif method == "":
        pass

    return mask, overwrite, mainline