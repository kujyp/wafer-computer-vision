import cv2
import numpy as np

from logics.regist.TemplateRegister import finddelta_withtemplate


def findregion_withvertices(image, vertices):
    mask = np.zeros_like(image)

    if len(image.shape) > 2:
        channel_count = image.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, vertices, ignore_mask_color)

    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def cropregion_withxy(image, xy):
    """
    
    :param image: 
    :param xy: (xst, yst, xed, yed) 
    :return: croppedimage
    """
    copy = np.copy(image)
    crop = copy[xy[1]:xy[3], xy[0]:xy[2]]
    return crop