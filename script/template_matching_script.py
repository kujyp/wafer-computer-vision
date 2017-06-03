from src.loadpic import load_allpath
from src.visualize.visualizer_numpy import show_mbyn_images
from tools.tool import *

dir = "data/내려놓은후_모든사진"

paths = load_allpath(dir)
imgs = []

for path in paths:
    imgs.append(cv2.imread(path))

path = "data/seg.png"
template = cv2.imread(path)


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
    # top_left[0] <- 이것
    #cv2.rectangle(img, top_left, bottom_right, 255, 2)
    #import matplotlib.pyplot as plt
    #plt.subplot(121), plt.imshow(res, cmap='gray')
    #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122), plt.imshow(img, cmap='gray')
    #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #plt.suptitle(meth)
    #plt.show()

def drawline(img,delta_x):
    x1, y1 = 298+(delta_x), 0
    x2, y2 = 282+(delta_x), 1090
    cv2.line(img, (x1, y1), (x2, y2), randomcolor(), 5)


# imgs = [imgs[0]]
show_imgs = []

img1 = imgs[0]
img2 = imgs[1]

import os
normal_img_path = os.path.join(dir,"ch01 normal ch2.png")
normal_img  = cv2.imread(normal_img_path)
normal_delta_x = (regist(normal_img, template))

def make_template_same_size(template, img, normal_delta_x):

    large_template = np.zeros(img.shape, dtype="uint8")

    large_template[:template.shape[0], normal_delta_x:normal_delta_x+template.shape[1]] = template[:, :]
    return large_template

def convert_to_red(img):
    mix_img = np.zeros([img.shape[0],img.shape[1],3],'uint8')
    black = np.zeros([img.shape[0], img.shape[1]],'uint8')
    if img.ndim is 3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mix_img[:,:,0] = img
    mix_img[:,:,1] = black
    mix_img[:,:,2] = black

    return mix_img


large_template = make_template_same_size(template, imgs[0], normal_delta_x)
#red_large_template = convert_to_red(large_template)
drawline(large_template,normal_delta_x)
#show_imgs.append(large_template)

st, ed = 0, 3
#st, ed = 3, 6
#st, ed = 6, 9

for idx, img in enumerate(imgs[st:ed]):
    delta_x = regist(img, template)
    drawline(img,delta_x)
    print(os.path.split(paths[idx])[-1])
    print(normal_delta_x - delta_x)
    added = cv2.addWeighted(img, 0.4, large_template, 0.6, 1)
    show_imgs.append(img)
    show_imgs.append(added)


show_mbyn_images(show_imgs, ed-st, 2)