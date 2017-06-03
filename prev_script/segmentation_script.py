import cv2
from src.loadpic import load_pics
from src.visualize.visualizer_numpy import show_mbyn_images
import numpy as np


def imshow_(img):
    cv2.imshow('processing',img)
    cv2.waitKey(0)

def randomcolor():
    import random
    import math
    r = math.floor(random.random() * 255)
    g = math.floor(random.random() * 255)
    b = math.floor(random.random() * 255)

    return (r,g,b)

def drawcontour(rgb, gray):
    img2, contours, hierarchy = cv2.findContours(gray.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        aspectratio = float(w) / h
        height, width = gray.shape
        pick_area = w * h
        total_area = width * height
        #extent = float(pick_area) / total_area
        extent = float(area) / total_area

        #if len(approx) == 4 and (extent) > 0.005:
        if extent > 0.005:
            cv2.drawContours(rgb, [c], -1, randomcolor(), 2)
        #imshow_(img)

def gradient(img):
    img_x = cv2.Sobel(img,-1,1,0)
    img_xy = img_x
    #img_y = cv2.Sobel(img,-1,0,1)
    #img_xy = np.power((np.power(img_x,2) + np.power(img_y,2)),1/2)
    img_xy = cv2.normalize(img_xy.astype('uint8'), None, 0, 255, cv2.NORM_MINMAX)
    return img_xy

def threshold(img, threshold=0.65):
    img_histeq = cv2.equalizeHist(img)
    return np.multiply(img, img_histeq > 255 * threshold)


dir = "data/내려놓은후_모든사진"
imgs = load_pics(dir)
#imgs = [imgs[0]]
show_imgs = []

for img in imgs[0:]:
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img2 = gradient(img2)

    img2 = threshold(img2,0.5)
    #img2 = img2_xy_2

    #show_imgs.append(result)

    #img2 = cv2.Canny(img2, 10, 200)

    #img2_xy_2 = cv2.adaptiveThreshold(img2_xy_2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #                                  cv2.THRESH_BINARY,11,2)
    #show_imgs.append(img2_xy_2)

    #show_imgs.append(img2)

    #img_canny_1 = cv2.Canny(img2, 0, 0)
    #show_imgs.append(img_canny_1)
    #img_canny_2 = cv2.Canny(img2, 1, 10)
    #show_imgs.append(img_canny_2)
    #img_canny_3 = cv2.Canny(img2, 1, 50)
    #show_imgs.append(img_canny_3)
    #img_canny_4 = cv2.Canny(img2, 1, 100)
    #show_imgs.append(img_canny_4)
    #img2 = cv2.GaussianBlur(img2, (3, 3), 0)
    #show_imgs.append(img2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9)) # 9 is best
    img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
    #show_imgs.append(img2)
    img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
    #show_imgs.append(img2)
    drawcontour(img, img2)
    show_imgs.append(img)



    #show_imgs.append(img)
show_mbyn_images(show_imgs,4,4)