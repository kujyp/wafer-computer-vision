import cv2


def subtractBackground(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    img = fgbg.apply(img)


    return img