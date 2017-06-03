from src.loadpic import load_pics
from src.visualize.visualizer_numpy import show_mbyn_images
from tools.tool import *


dir = "data/내려놓은후_모든사진"
imgs = load_pics(dir)
path = "data/seg.png"
template = cv2.imread(path)


def regist(img, template):

    pass

# imgs = [imgs[0]]
show_imgs = []

img1 = imgs[0]
img2 = imgs[1]

img2 = np.zeros(img1.shape)
img2[:template.shape[0],:template.shape[1]] = template[:,:]
img2 = img2.astype('uint8')

img3 = regist(img1,template)

sum_img = cv2.addWeighted(img1,0.5,img2,0.5,1)


#show_imgs.append(img3)
show_imgs.append(sum_img)
# img3 = matcher(img2,template)
# #show_imgs.append(img3)

show_mbyn_images(show_imgs, 1, 2)