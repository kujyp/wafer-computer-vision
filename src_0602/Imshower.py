import cv2


def imgshow(img, windowName, dsize=None):
    if dsize is not None:
        img = cv2.resize(img, dsize)
    cv2.imshow(windowName,img)