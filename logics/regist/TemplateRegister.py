import cv2

import numpy as np

TEXT_X_MARGIN = 50
TEXT_FONTSIZE = 2
TEXT_LINEWIDTH = 4

def regist(img, template):
    w, h = template.shape[1::-1]

    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #       'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    meth = 'cv2.TM_CCOEFF_NORMED'
    #img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    #template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    #for meth in methods:
    img = img.copy()

    method = eval(meth)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    return top_left[0]

def findDelta(img, template):
    normal_delta_x = (regist(img, template))
    return normal_delta_x

def drawNormalRectangle(image, seg):
    copy = np.copy(image)
    templatex = 845
    xst, xed = templatex, templatex+(1130-845) # Video4 Normal
    yst, yed = 0, image.shape[0]

    delta = seg - templatex

    cv2.rectangle(copy, (xst, yst), (xed, yed), (255, 0, 0), 3)
    cv2.putText(copy, "xst,yst={},{}".format(xst, yst+100), (xed + TEXT_X_MARGIN, yst + 50+100),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (255, 0, 0), TEXT_LINEWIDTH, cv2.LINE_AA)
    cv2.putText(copy, "xed,yed={},{}".format(xed, yed+100), (xed + TEXT_X_MARGIN, yst + 100+100),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (255, 0, 0), TEXT_LINEWIDTH, cv2.LINE_AA)

    cv2.putText(copy, "delta={}".format(delta), (xed + TEXT_X_MARGIN, yst + 100 + 150),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONTSIZE, (0, 0, 255), TEXT_LINEWIDTH, cv2.LINE_AA)

    return copy


