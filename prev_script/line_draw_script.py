from src.loadpic import load_pics
from src.visualize.visualizer_numpy import show_mbyn_images
from tools.tool import *


dir = "data/내려놓은후_모든사진"
imgs = load_pics(dir)
path = "data/seg.png"
template = cv2.imread(path)

# imgs = [imgs[0]]
show_imgs = []


x1, y1 = 298, 0
x2, y2 = 282, 1090
cv2.line(template, (x1, y1), (x2, y2), randomcolor(), 5)

show_imgs.append(template)


img1 = imgs[0]
img2 = imgs[1]
show_mbyn_images(show_imgs, 1, 2)