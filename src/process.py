import cv2


def drawcontour(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imshow_(img2)
    img2 = cv2.Canny(img2, 50, 500)
    imshow_(img2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    #img2 = cv2.morphologyEx(img2 , cv2.MORPH_CLOSE, kernel)
    imshow_(img2)
    img2, contours, hierarchy = cv2.findContours(img2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        aspectratio = float(w) / h
        height, width, channels = img.shape
        pick_area = w * h
        total_area = width * height
        #extent = float(pick_area) / total_area
        extent = float(area) / total_area

        #if len(approx) == 4 and (extent) > 0.005:
        cv2.drawContours(img, [approx], -1, (255, 0, 0), 1)
        imshow_(img)

    return img

def imshow_(img):
    cv2.imshow('processing',img)
    cv2.waitKey(0)