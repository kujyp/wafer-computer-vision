import cv2
import numpy as np


def findInterestRegion(image):
    imshape = image.shape
    vertices = np.array([[(0, imshape[0]), (450, 320), (500, 320), (imshape[1], imshape[0])]], dtype=np.int32)
    masked = region_of_interest(image, vertices)

    return masked

def region_of_interest(image, vertices):
    # defining a blank mask to start with
    mask = np.zeros_like(image)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(image.shape) > 2:
        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image