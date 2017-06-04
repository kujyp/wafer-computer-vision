from logics.corner_detector import detectCornerWithFAST
from logics.hough_line_detector import detectHoughLines


def convertFeatureMap(image, method="hough"):
    img = image[:]
    mask, overwrite, mainline = None, None, None
    if method == "hough":
        mask, overwrite, mainline = detectHoughLines(img)
    elif method == "fast":
        mask = detectCornerWithFAST(img)
    elif method == "":
        pass

    return mask, overwrite, mainline