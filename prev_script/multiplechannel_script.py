from src.loadpic import load_pics
from src.visualize.visualizer_numpy import show_mbyn_images
from tools.tool import *


dir = "data/내려놓은후_모든사진"
imgs = load_pics(dir)
# imgs = [imgs[0]]
show_imgs = []

for img in imgs[0:1]:
    img_rgb = cv2.split(img)

    show_imgs.append(img_rgb[0])
    show_imgs.append(img_rgb[1])
    show_imgs.append(img_rgb[2])

show_mbyn_images(show_imgs, 2, 4)