import cv2
import numpy as np


def findregion_withvertices(image, vertices):
    """
    image를 4개의 변을 따라 사각형으로 잘라냄
    
    :param image: 원본 이미지
    :param vertices: 4개의 변. 예시=[(xst, yst), (xst, yed), (xed, yed), (xed, yst)]
    :return: 잘려진 bitwise 이미지
    """
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
    사각형으로 이미지를 잘라냄
    
    :param image: 원본이미지
    :param xy: 잘려질 이미지의 시작/끝 좌표, (xst, yst, xed, yed) 순서 
    :return: croppedimage
    """
    copy = np.copy(image)
    crop = copy[xy[1]:xy[3], xy[0]:xy[2]]
    return crop