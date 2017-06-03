from src.loadpic import load_pics
import numpy as np

from src.loadpic import load_pics
from src.visualize.visualizer_numpy import show_mbyn_images
from tools.tool import *

dir = "data/내려놓은후_모든사진"
imgs = load_pics(dir)
# imgs = [imgs[0]]
show_imgs = []

for img in imgs[0:1]:
    lsd_img = lsd(img)
    #show_imgs.append(lsd_img)

    #lsd_img = cv2.cvtColor(lsd_img, cv2.COLOR_BGR2GRAY)
    lsd_img = lsd_img.astype('uint8')
    show_imgs.append(lsd_img)

    lines = cv2.HoughLines(lsd_img, 1, np.pi / 180, 100)
    # print(lines)

    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), randomcolor(), 5)
    show_imgs.append(img)

show_mbyn_images(show_imgs, 2, 4)