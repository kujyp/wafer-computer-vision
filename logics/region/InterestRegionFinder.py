import cv2
import numpy as np


TEXT_X_MARGIN = 50
TEXT_FONTSIZE = 1.5
TEXT_LINEWIDTH = 3
TEXT_LINESPACING = 50
TEXT_TOPLINESPACING = 100

def findInterestRegion(image):
    imshape = image.shape

    deltax = 845
    xst, xed = deltax, deltax+(1130-845)
    # xst, xed = 845, 1130 # Video4
    yst, yed = 0, imshape[0]
    vertices = np.array([[(xst-50, yst), (xst-50, yed), (xed+50, yed), (xed+50, yst)]], dtype=np.int32)

    masked = region_of_interest(image, vertices)

    deltax = 150
    xst, xed = deltax, deltax + (1130 - 845)
    # xst, xed = 845, 1130 # Video4
    yst, yed = 0, imshape[0]
    vertices = np.array([[(xst - 50, yst), (xst - 50, yed), (xed + 50, yed), (xed + 50, yst)]], dtype=np.int32)

    masked2 = region_of_interest(image, vertices)

    added = cv2.addWeighted(masked, 1, masked2, 1,0)

    return added

def drawNormalRectangle(image):
    copy = np.copy(image)
    templatex = 845
    xst, xed = templatex, templatex+(1130-845) # Video4 Normal
    yst, yed = 0, image.shape[0]


    cv2.rectangle(copy, (xst, yst), (xed, yed), (255, 0, 0), 3)
    cv2.putText(copy, "Set Normal", (xed + TEXT_X_MARGIN, yst + TEXT_LINESPACING+TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (255, 0, 0), TEXT_LINEWIDTH, cv2.LINE_AA)
    cv2.putText(copy, "x=[{}-{}]".format(xst, xed), (xed + TEXT_X_MARGIN, yst + TEXT_LINESPACING*2+TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (255, 0, 0), TEXT_LINEWIDTH, cv2.LINE_AA)

    result_msg = ""
    cv2.putText(copy, result_msg, (xed + TEXT_X_MARGIN, yst + TEXT_LINESPACING*4+ TEXT_TOPLINESPACING),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (0, 0, 255), TEXT_LINEWIDTH, cv2.LINE_AA)

    return copy

# def findInterestRegion(image):
#     imshape = image.shape
#     vertices = np.array([[(0, imshape[0]), (450, 320), (500, 320), (imshape[1], imshape[0])]], dtype=np.int32)
#     masked = region_of_interest(image, vertices)
#
#     return masked

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