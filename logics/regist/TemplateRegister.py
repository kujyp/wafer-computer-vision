import cv2


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